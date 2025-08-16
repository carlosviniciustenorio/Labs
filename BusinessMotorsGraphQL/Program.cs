using BusinessMotorsGraphQL.Queries;
using BusinessMotorsGraphQL.Services;
using BusinessMotorsGraphQL.Mutations;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddSingleton<CarroService>();
builder.Services.AddGraphQLServer()
                .AddQueryType<CarroQuery>()
                .AddMutationType<CarroMutation>();

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