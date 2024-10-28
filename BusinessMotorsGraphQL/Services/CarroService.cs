using BusinessMotorsGraphQL.Model;

namespace BusinessMotorsGraphQL.Services;

public class CarroService
{
    private readonly List<Carro> _carros = new()
    {
        new Carro { Id = 1, Marca = "Toyota", Modelo = "Corolla" },
        new Carro { Id = 2, Marca = "Ford", Modelo = "Fiesta" },
        new Carro { Id = 3, Marca = "Honda", Modelo = "Civic" }
    };

    public IEnumerable<Carro> GetCarros() => _carros;
}