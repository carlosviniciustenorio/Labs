using BusinessMotorsGraphQL.Model;
using BusinessMotorsGraphQL.Services;

namespace BusinessMotorsGraphQL.Queries;

public class CarroQuery
{
    private readonly CarroService _carroService;

    public CarroQuery(CarroService carroService)
    {
        _carroService = carroService;
    }

    public IEnumerable<Carro> GetCarros() => _carroService.GetCarros();
}