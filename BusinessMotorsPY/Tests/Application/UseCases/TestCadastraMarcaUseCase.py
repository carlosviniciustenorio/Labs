from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch
from Application.DTOs.Request.InsertMarcaDTO import InsertMarcaDTO
from Domain.Entities.Marca import Marca
from Application.UseCases.CadastraMarcaUseCase import CadastraMarcaUseCase


class TestCadastraMarcaUseCase(IsolatedAsyncioTestCase):

    @patch('Infrastructure.Repositories.MarcaRepository')
    async def test_execute(self, MockMarcaRepository):
        # Arrange
        mock_repo = MockMarcaRepository.return_value
        mock_repo.insert = AsyncMock(return_value="success")

        db = None
        use_case = CadastraMarcaUseCase(db)

        marca_dto = InsertMarcaDTO(Descricao="Marca Teste")

        # Act
        result = await use_case.execute(marca_dto)

        # Assert
        mock_repo.insert.assert_called_once()
        self.assertEqual(result, "success")
