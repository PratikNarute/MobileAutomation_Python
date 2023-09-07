from time import sleep

import pytest
from self import self

import pages.productType
import testCases.test_2ProductType
from pages.loginPage import LoginPage
from pages.productType import ProductType



name = ""


class Test_ProductType:

    @pytest.fixture(autouse=True)
    def objects(self):
        self.pt = ProductType(self.driver)
        self.lg = LoginPage(self.driver)

    def test_create_product_type_with_positive_data(self):
        global name
        self.lg.login()
        sleep(2)
        self.pt.createProductWithPositiveData()

    def test_impact_of_created_product_type(self):
        global name
        name = pages.productType.name
        self.pt.to_check_that_impact_of_created_product_type_on_the_product_type_table_list(name)

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_create_product_type_with_negative_data(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_edit_product_type_with_positive_data(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_impact_of_edit_product_type(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_edit_product_type_with_negative_data(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_functional_flow_or_navigation_of_product_type(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_sorting_of_product_list_page(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_searching_functionality_of_product_list_page(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_product_type_scenarios_as_per_role_permission_wise(self):
        pass

    @pytest.mark.skip(reason="Test case is not ready yet")
    def test_product_type_scenarios_as_per_organization_wise(self):
        pass
