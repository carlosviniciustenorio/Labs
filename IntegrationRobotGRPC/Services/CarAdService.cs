using CarAdService;
using IntegrationRobotGRPC.Models;
using Grpc.Core;

namespace IntegrationRobotGRPC.Services;
public class CarAdService : CarAd.CarAdBase
{
    private readonly CarAdDatabase _database;

    public CarAdService(CarAdDatabase database)
    {
        _database = database;
    }

    public override Task<UpdateCarAdReply> UpdateCarAd(UpdateCarAdRequest request, ServerCallContext context)
    {
        var ad = new CarAdEntity
        {
            Id = request.Id,
            Title = request.Title,
            Description = request.Description,
            Price = request.Price
        };

        _database.UpdateAd(ad);

        return Task.FromResult(new UpdateCarAdReply
        {
            Message = "Car ad updated successfully"
        });
    }
}
