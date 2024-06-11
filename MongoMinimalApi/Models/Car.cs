using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using MongoMinimalApi.DTOs;

namespace MongoMinimalApi.Models;

public class Car
{
    [BsonId]
    [BsonRepresentation(BsonType.String)]
    public Guid Id { get; init; } = Guid.NewGuid();
    public string Make { get; set; }
    public string Model { get; set; }
    public int Year { get; set; }

    public void Update(CarPutDTO car) => (Make, Model, Year) = (car.Make, car.Model, car.Year);
}