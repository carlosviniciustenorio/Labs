using BusinessMotorsGraphQL.Model;
using BusinessMotorsGraphQL.Services;

namespace BusinessMotorsGraphQL.Mutations;

public class CarroMutation
{
    private readonly CarroService _carroService;

    public CarroMutation(CarroService carroService)
    {
        _carroService = carroService;
    }

    public Carro AdicionarCarro(string marca, string modelo)
    {
        var novoCarro = new Carro
        {
            Marca = marca,
            Modelo = modelo
        };

        _carroService.AdicionarCarro(novoCarro);
        return novoCarro;
    }
}
