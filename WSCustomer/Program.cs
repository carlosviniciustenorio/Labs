using System.Net.WebSockets;
using System.Text;
using WSCustomer;

var connectionPool = new WebSocketConnectionPool("ws://localhost:5273/", 10);
for (int i = 0; i < 20; i++) // Simulando 20 solicitações
{
    var connection = await connectionPool.GetConnectionAsync();
    Console.WriteLine($"Enviando solicitação {i + 1}");

    while(connection.State == WebSocketState.Open)
    {
        var buffer = new byte[256];
        var result = await connection.ReceiveAsync(buffer, CancellationToken.None);
        
        if (result.MessageType == WebSocketMessageType.Close)
            await connection.CloseAsync(WebSocketCloseStatus.NormalClosure, null, CancellationToken.None);
        else
            Console.WriteLine(Encoding.ASCII.GetString(buffer, 0, result.Count));
        
    }
    connectionPool.ReleaseConnection(connection);
}