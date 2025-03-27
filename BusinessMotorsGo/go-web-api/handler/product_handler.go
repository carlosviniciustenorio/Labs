package handler

import (
	"go-web-api/domain"
	"go-web-api/usecase"
	"net/http"

	"github.com/gin-gonic/gin"
)

type ProductHandler struct {
	useCase *usecase.ProductUseCase
}

func NewProductHandler(u *usecase.ProductUseCase) *ProductHandler {
	return &ProductHandler{useCase: u}
}

func (h *ProductHandler) CreateProduct(c *gin.Context) {
	var product domain.Product
	if err := c.ShouldBindJSON(&product); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	if err := h.useCase.CreateProduct(product); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not create product"})
		return
	}
	c.JSON(http.StatusCreated, product)
}

func (h *ProductHandler) GetProducts(c *gin.Context) {
	products, err := h.useCase.GetAllProducts()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not fetch products"})
		return
	}
	c.JSON(http.StatusOK, products)
}
