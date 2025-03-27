package domain

type Product struct {
	ID    uint    `gorm:"primaryKey"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}

type ProductRepository interface {
	Save(product Product) error
	GetAll() ([]Product, error)
}
