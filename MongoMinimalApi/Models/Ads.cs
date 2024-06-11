using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace MongoMinimalApi.Models;

public class Ads
{
    [BsonId]
    [BsonRepresentation(BsonType.String)]
    public Guid Id { get; set; }
    public DateTime CreatedAt { get; init; } = DateTime.Now;
    [BsonRepresentation(BsonType.String)]
    public Guid CarId { get; set; }
}