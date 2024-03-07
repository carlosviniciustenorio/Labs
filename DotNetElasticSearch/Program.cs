using System;
using Elasticsearch.Net;
using Nest;

class Program
{
    static void Main(string[] args)
    {
        var settings = new ConnectionSettings(new Uri("http://localhost:9200"))
            .DefaultIndex("cmanager");

        var client = new ElasticClient(settings);

        var response = client.IndexDocument(new Car(){ Id = 3, Marca = "Fiat", Nome = "Palio"});
        if (response.IsValid)
        {
            Console.WriteLine("Documento criado com sucesso!");
        }
        else
        {
            Console.WriteLine($"Erro ao criar documento: {response.DebugInformation}");
        }
        
        var searchResponse = client.Search<Car>(s => s
            .Query(q => q
                .Match(m => m
                    .Field(f => f.Marca.ToUpper())
                    .Query("JEEP")
                )
            )
        );

        if (searchResponse.IsValid)
        {
            foreach (var hit in searchResponse.Hits)
            {
                Console.WriteLine($"Documento encontrado: {hit.Source.Nome}");
            }
        }
        else
        {
            Console.WriteLine($"Erro ao executar a busca: {searchResponse.DebugInformation}");
        }
    }
}

public class Car
{
    public int Id { get; set; }
    public string Nome { get; set; }
    public string Marca { get; set; }
}
