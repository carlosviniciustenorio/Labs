using IntegrationRobotGRPC.Models;
using IntegrationRobotGRPC.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<CarAdDatabase>();
builder.Services.AddGrpc();
builder.Services.AddGrpcReflection();

builder.WebHost.ConfigureKestrel(options =>
{
    options.ListenAnyIP(7073, listenOptions =>
    {
        listenOptions.Protocols = Microsoft.AspNetCore.Server.Kestrel.Core.HttpProtocols.Http2;
    });
});

var app = builder.Build();

app.MapGrpcService<GreeterService>();
app.MapGrpcService<IntegrationRobotGRPC.Services.CarAdService>();

if (app.Environment.IsDevelopment())
{
    app.MapGrpcReflectionService();
}

app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
