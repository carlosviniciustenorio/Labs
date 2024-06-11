using Microsoft.OpenApi.Models;
using MongoDB.Driver;
using MongoMinimalApi.DTOs;
using MongoMinimalApi.Models;
using MongoMinimalApi.Services;
using MongoMinimalApi.Settings;

var builder = WebApplication.CreateBuilder(args);
builder.Services.Configure<MongoDbSettings>(builder.Configuration.GetSection("MongoDbSettings"));

builder.Services.AddSingleton<IMongoClient, MongoClient>(
    sp => new MongoClient(builder.Configuration.GetValue<string>("MongoDbSettings:ConnectionString")));

builder.Services.AddSingleton<CarService>();
builder.Services.AddHttpClient();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo { Title = "Car API", Version = "v1" });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c =>
    {
        c.SwaggerEndpoint("/swagger/v1/swagger.json", "Car API V1");
        c.RoutePrefix = string.Empty; // Serve Swagger UI at the app's root
    });
}

app.MapGet("/cars", async (CarService carSerivce) => await carSerivce.GetAsync());

app.MapGet("/cars/{id}", async (Guid id, CarService carService) =>
{
    Car car = await carService.GetAsync(id);
    return car is not null ? Results.Ok(car) : Results.NotFound();
});

app.MapPost("/cars", async (Car newCar, CarService carService) =>
{
    await carService.CreateAsync(newCar);
    return Results.Created($"/cars/{newCar.Id}", newCar);
});

app.MapPut("/cars/{id}", async (Guid key, CarPutDTO carToUpdate, CarService carService) =>
{
    Car car = await carService.GetAsync(key);
    if (car is null)
        return Results.NotFound();
    
    car.Update(carToUpdate);

    await carService.UpdateAsync(key, car);
    return Results.NoContent();
});

app.MapDelete("/cars/{id}", async (Guid key, CarService carService) =>
{
    Car car = await carService.GetAsync(key);
    if (car is null)
        return Results.NotFound();

    await carService.RemoveAsync(key);
    return Results.NotFound();
});

app.MapPost("/ads", async (Ads ads, CarService carService) =>
{
    await carService.CreateAdsAsync(ads);
    return Results.Created($"/ads/{ads.Id}", ads);
});

app.MapGet("/test", async (IHttpClientFactory factory) =>
{
    var client = factory.CreateClient();
    client.BaseAddress = new Uri("https://google.com");
    client.Timeout = TimeSpan.FromSeconds(10);
    var result = await client.GetAsync("search?q=test");
    return Results.Ok(result);
});

app.Run();
