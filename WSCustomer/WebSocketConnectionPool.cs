using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.WebSockets;
using System.Threading.Tasks;

namespace WSCustomer
{
    public class WebSocketConnectionPool
    {
        private readonly string _serverUri;
        private readonly List<ClientWebSocket> _connections;
        private readonly SemaphoreSlim _semaphore;

        public WebSocketConnectionPool(string serverUri, int poolSize)
        {
            _serverUri = serverUri;
            _connections = new List<ClientWebSocket>();
            _semaphore = new SemaphoreSlim(poolSize, poolSize);
        }

        public async Task<ClientWebSocket> GetConnectionAsync()
        {
            await _semaphore.WaitAsync();

            ClientWebSocket connection = null;
            lock (_connections)
            {
                if (_connections.Count > 0)
                {
                    connection = _connections[0];
                    _connections.RemoveAt(0);
                }
            }

            if (connection == null)
            {
                connection = new ClientWebSocket();
                Console.WriteLine("Criando e adicionando conexão novamente ao pool");
                await connection.ConnectAsync(new Uri(_serverUri), CancellationToken.None);
            }

            return connection;
        }

        public void ReleaseConnection(ClientWebSocket connection)
        {
            lock (_connections)
            {
                _connections.Add(connection);
                Console.WriteLine("Adicionando conexão existente novamente ao pool");
            }
            _semaphore.Release();
        }
    }

}