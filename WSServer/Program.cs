using System.Net.WebSockets;
using System.Text;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

app.UseWebSockets();
app.Map("/", async context =>
{
    double cotacao = 1.10;
    if (!context.WebSockets.IsWebSocketRequest)
        context.Response.StatusCode = 400;
    else
    {
        using var webSocket = await context.WebSockets.AcceptWebSocketAsync();
        while (true)
        {
            await webSocket.SendAsync(
                Encoding.ASCII.GetBytes($"Preco da cotacão ITUB3: {cotacao}"),
                WebSocketMessageType.Text,
                true, CancellationToken.None);
            await Task.Delay(1000);
            Console.WriteLine($"Cotação: {cotacao}");
            cotacao += 1;
        }
    }
});
await app.RunAsync();


record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
