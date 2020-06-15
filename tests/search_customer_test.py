from tests.test import test
from search_customer import search

correct_1 = [ "Gasai\tYuno\t(+81)120-389-123", "Amano\tYukiteru\t(+81)783-124-632" ]
test( search, [ "customers", "Yu" ], correct_1 )

correct_2 = [ "Gasai\tYuno\t(+81)120-389-123", "Deus\tExMachina\t(+81)777-666-120" ]
test( search, [ "customers", "120" ], correct_2 )

correct_3 = [ ]
test( search, [ "customers", "Carrot" ], correct_3 )