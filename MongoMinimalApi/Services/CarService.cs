using Microsoft.Extensions.Options;
using MongoDB.Driver;
using MongoMinimalApi.Models;
using MongoMinimalApi.Settings;

namespace MongoMinimalApi.Services;

public class CarService
{
    private readonly IMongoCollection<Car> _carsCollection;
    private readonly IMongoCollection<Ads> _adsCollection;

    public CarService(IOptions<MongoDbSettings> mongoDbSettings, IMongoClient mongoClient)
    {
        var mongoDatabase = mongoClient.GetDatabase(mongoDbSettings.Value.DatabaseName);
        _carsCollection = mongoDatabase.GetCollection<Car>("Cars");
        _adsCollection = mongoDatabase.GetCollection<Ads>("Ads");
    }

    public async Task<List<Car>> GetAsync() => await _carsCollection.Find(_ => true).ToListAsync();

    public async Task<Car> GetAsync(Guid id) => await _carsCollection.Find(x => x.Id == id).FirstOrDefaultAsync();

    public async Task CreateAsync(Car newCar) => await _carsCollection.InsertOneAsync(newCar);
    public async Task CreateAdsAsync(Ads ads) => await _adsCollection.InsertOneAsync(ads);

    public async Task UpdateAsync(Guid id, Car updatedCar) => await _carsCollection.ReplaceOneAsync(x => x.Id == id, updatedCar);

    public async Task RemoveAsync(Guid id) => await _carsCollection.DeleteOneAsync(x => x.Id == id);
}