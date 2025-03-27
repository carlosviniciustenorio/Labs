package usecase

import "go-web-api/domain"

type ProductUseCase struct {
	repo domain.ProductRepository
}

func NewProductUseCase(r domain.ProductRepository) *ProductUseCase {
	return &ProductUseCase{repo: r}
}

func (u *ProductUseCase) CreateProduct(product domain.Product) error {
	return u.repo.Save(product)
}

func (u *ProductUseCase) GetAllProducts() ([]domain.Product, error) {
	return u.repo.GetAll()
}
