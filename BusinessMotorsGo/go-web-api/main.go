package main

import (
	"go-web-api/config"
	"go-web-api/handler"
	"go-web-api/infrastructure"
	"go-web-api/usecase"

	"github.com/gin-gonic/gin"
)

func main() {
	db := config.InitDB()

	productRepo := infrastructure.NewProductRepository(db)
	productUseCase := usecase.NewProductUseCase(productRepo)
	productHandler := handler.NewProductHandler(productUseCase)

	r := gin.Default()
	r.POST("/products", productHandler.CreateProduct)
	r.GET("/products", productHandler.GetProducts)

	r.Run(":8080")
}
