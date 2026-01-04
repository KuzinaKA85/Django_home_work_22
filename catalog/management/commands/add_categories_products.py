from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add categories, products to the database"

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category1 = Category.objects.create(
            name_category="Пылесосы",
            description_category="Устройство, незаменимое в процессе уборки, ведь с его помощью вы сможете за "
            "считанные минуты очистить любое напольное покрытие от мусора и пыли.",
        )

        category2 = Category.objects.create(
            name_category="Утюги",
            description_category="Элемент бытовой техники для разглаживания складок и заминов на одежде.",
        )

        category3 = Category.objects.create(
            name_category="Стиральные машины",
            description_category="Элемент бытовой техники для стирки белья.",
        )

        products = [
            {
                "name_product": "Пылесос Samsung SC4581",
                "description_product": "Пылесос предназначен для сухой уборки со сбором мусора в контейнер. "
                "Есть встроенная защита двигателя от перегрева. Циклонная система фильтрации хорошо "
                "улавливает мелкую пыль, сохраняет стабильную мощность всасывания и облегчает очистку "
                "контейнера. Пылесос оснащен насадками для очистки разных типов поверхностей.",
                "category_product": category1,
                "price_product": 5499.0,
            },
            {
                "name_product": "Пылесос Thomas DryBOX",
                "description_product": "Пылесос Thomas DryBOX выполнен в корпусе черного цвета с голубыми деталями. "
                "Вам понравится уникальный дизайн этой модели. Но куда важнее технические "
                "характеристики пылесоса.Thomas DryBOX AMFIBIA подходит для выполнения как влажной, "
                "так и сухой уборки.",
                "category_product": category1,
                "price_product": 8499.0,
            },
            {
                "name_product": "Пылесос Philips FC2546",
                "description_product": "Типом пылесборника пылесоса Philips FC2546 стал циклонный фильтр, что "
                "обеспечивает высокую результативность сухой уборки, предельную мощность всасывания, удержание "
                "мельчайших частиц пыли с фильтром тонкой очистки. Функция Allergy Lock – просто "
                "идеальна для аллергиков.",
                "category_product": category1,
                "price_product": 13699.0,
            },
            {
                "name_product": "Утюг Polaris 355",
                "description_product": "Утюг Polaris 355 в стильном исполнении способен сделать процесс глажки  "
                "достаточно удобным и быстрым. Мощность утюга в 2400 Вт обеспечивает практически мгновенный "
                "нагрев рабочей поверхности. По периметру подошвы предусмотрен желобок для пуговиц, "
                "чтобы можно было легко проглаживать блузки и рубашки. Встроенный резервуар для воды "
                "вмещает 350 мл жидкости.",
                "category_product": category2,
                "price_product": 3499.0,
            },
            {
                "name_product": "Утюг Tefal Puregliss",
                "description_product": "Утюг Tefal Puregliss оснащен ударом со скоростью 280 г/мин, который быстро "
                "справится с непокорными заломами. Режим вертикального отпаривания поможет придать "
                "эстетичный вид тюлю и шторам. Функция разбрызгивания воды незаменима при устранении "
                "пересушенных участков.",
                "category_product": category2,
                "price_product": 7599.0,
            },
            {
                "name_product": "Утюг Braun 2125",
                "description_product": "Утюг Braun SI7181VI в фиолетовом корпусе легко скользит по поверхности "
                "отглаживаемого белья благодаря подошве высокой гладкости с канавкой для "
                "пуговиц EloxalPlus FreeGlide 3D, выполненной из алюминия. Для этой модели с "
                "потребляемой мощностью 3100 Вт характерно эффективное отпаривание.",
                "category_product": category2,
                "price_product": 9799.0,
            },
            {
                "name_product": "Стиральная машина LG FGD755",
                "description_product": "Стиральная машина LG FGD755 с фронтальной загрузкой способна очищать сразу "
                "до 7 кг белья. Это значит, что в бак поместятся одновременно до 2 одеял или пуховиков. "
                "Для стирки и того, и другого машина имеет специальные программы. Всего она оснащена "
                "13 режимами и опцией обработки выстиранного белья горячим паром.",
                "category_product": category3,
                "price_product": 39799.0,
            },
            {
                "name_product": "Стиральная машина Indesit EDST",
                "description_product": "Стиральная машина Indesit EDST с загрузкой до 5 кг белья и максимальной "
                "скоростью отжима 1000 об/мин получила специальный датчик Water Balance Plus. С его помощью "
                "регулируется расход воды исходя из загрузки белья, благодаря чему обеспечивается "
                "экономия энергопотребления, расхода воды и времени, затрачиваемого на стирку.",
                "category_product": category3,
                "price_product": 32499.0,
            },
            {
                "name_product": "Стиральная машина Haier HTD",
                "description_product": "Стиральная машина Haier HTD с фронтальной загрузкой на 5 кг оснащена "
                "барабаном Pillow. Отверстия в виде подушечек не провоцируют порчу материалов и гарантируют "
                "бережное устранение стойких загрязнений. Конструкцией люка предусмотрена манжета, "
                "предупреждающая развитие бактерий.",
                "category_product": category3,
                "price_product": 42199.0,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {product.name_product}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exist: {product.name_product}")
                )
