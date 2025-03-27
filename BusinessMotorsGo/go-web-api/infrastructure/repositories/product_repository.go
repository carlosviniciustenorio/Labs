package infrastructure

import (
	"go-web-api/domain"

	"gorm.io/gorm"
)

type ProductRepositoryImpl struct {
	DB *gorm.DB
}

func NewProductRepository(db *gorm.DB) domain.ProductRepository {
	return &ProductRepositoryImpl{DB: db}
}

func (r *ProductRepositoryImpl) Save(product domain.Product) error {
	return r.DB.Create(&product).Error
}

func (r *ProductRepositoryImpl) GetAll() ([]domain.Product, error) {
	var products []domain.Product
	err := r.DB.Find(&products).Error
	return products, err
}
