namespace IntegrationRobotGRPC.Models;

using System.Collections.Generic;

public class CarAdDatabase
{
    // Simulação de um banco de dados em memória
    private readonly Dictionary<string, CarAdEntity> _ads = new();

    public CarAdEntity GetAdById(string id)
    {
        _ads.TryGetValue(id, out var ad);
        return ad;
    }

    public void UpdateAd(CarAdEntity ad)
    {
        _ads[ad.Id] = ad;
    }
}

public class CarAdEntity
{
    public string Id { get; set; }
    public string Title { get; set; }
    public string Description { get; set; }
    public double Price { get; set; }
}
