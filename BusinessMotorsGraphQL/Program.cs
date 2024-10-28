using BusinessMotorsGraphQL.Queries;
using BusinessMotorsGraphQL.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddSingleton<CarroService>();
builder.Services.AddGraphQLServer()
                .AddQueryType<CarroQuery>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseRouting();
app.UseEndpoints(endpoints =>
{
    endpoints.MapGraphQL();
});

app.Run();