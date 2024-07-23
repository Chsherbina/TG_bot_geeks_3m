class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        visit_date DATE NOT NULL,
        food_rating INTEGER NOT NULL,
        cleanliness_rating INTEGER NOT NULL,
        extra_comments TEXT NOT NULL        
    )
    """

    DROP_CATEGORIES = "DROP TABLE IF EXISTS categories"

    CREATE_CATEGORIES_TABLE="""
        CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        UNIQUE(name))"""

    POPULATE_CATEGORIES = """
        INSERT OR IGNORE INTO categories(name) VALUES
            ('салаты'),
            ('первое'),
            ('второе'),
            ('десерты')
        """

    DROP_DISHES = "DROP TABLE IF EXISTS dishes"

    CREATE_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        weight INTEGER,
        composition TEXT,
        price INTEGER,
        photo TEXT,
        catrgories_id INTEGER,
        UNIQUE(name),
        FOREIGN KEY(catrgories_id) REFERENCES categories (id))
        """


    POPULATE_DISHES = """
    INSERT OR IGNORE INTO dishes(name, weight, composition, price, photo, catrgories_id) VALUES
    ('Цезарь с креветками', 220, 'Листья салата, креветки, сыр пармезан, сухарики, соус цезарь', 280, 'images/Цезарь с креветками.jpg', 1),
    ('Оливье', 140, 'Картофель, морковь, горошек, соленые огурцы, колбаса, майонез', 200, 'images/Цезарь с креветками.jpg', 1),
    ('Винегрет', 120, 'Свекла, картофель, морковь, соленые огурцы, лук, растительное маслa', 200, 'images/Цезарь с креветками.jpg', 1),
    ('Капрезе', 170, 'Помидоры, моцарелла, базилик, оливковое масло, бальзамический уксус', 180, 'images/Цезарь с креветками.jpg', 1),
    ('Суп-лапша с курицей', 20, 'Куриный бульон, лапша, курица, морковь, картофель, лук, зелень', 350, 'images/Цезарь с креветками.jpg', 2),
    ('Куриный суп с фрикадельками', 130, 'Куриный бульон, фрикадельки из куриного фарша, картофель, морковь, лук, зелень', 350, 'images/Цезарь с креветками.jpg', 2),
    ('Солянка мясная', 160, 'Говяжий бульон, говядина, сосиски, маринованные огурцы, оливки, томатная паста, картофель, лук, зелень', 350, 'images/Цезарь с креветками.jpg', 2),
    ('Щи с грибами', 140, 'Свекольный бульон, капуста, картофель, морковь, лук, грибы, томатная паста, зелень', 350, 'images/Цезарь с креветками.jpg', 2),
    ('Уха рыбная', 180, 'Рыбный бульон, рыба, картофель, морковь, лук, зелень', 400, 'images/Цезарь с креветками.jpg', 2),
    ('Рыбные палочки с гарниром', 190, 'Рыбные палочки, рис, овощной салат', 250, 'images/Цезарь с креветками.jpg', 3),
    ('Куриные крылышки в медово-соевом соусе', 160, 'Куриные крылышки, медово-соевый соус', 200, 'images/Цезарь с креветками.jpg', 3),
    ('Пельмени с мясом', 170, 'Пельмени с мясным фаршем, сметана', 300, 'images/Цезарь с креветками.jpg', 3),
    ('Голубцы с мясом и рисом', 180, 'Голубцы с мясным фаршем и рисом, томатный соус', 250, 'images/Цезарь с креветками.jpg', 3),
    ('Картофельные драники со сметаной', 140, 'Картофельные драники, сметана', 200, 'images/Цезарь с креветками.jpg', 3),
    ('Шоколадный торт', 180, 'Шоколадный бисквит, шоколадный крем, глазурь', 150, 'images/Цезарь с креветками.jpg', 4),
    ('Творожный десерт с ягодами', 150, 'Творожная масса, свежие ягоды, мёд', 120, 'images/Цезарь с креветками.jpg', 4),
    ('Тирамису', 170, 'Савоярди, маскарпоне, кофе, какао', 130, 'images/Цезарь с креветками.jpg', 4),
    ('Панкейки с фруктами', 160, 'Панкейки, фрукты (ягоды, бананы), сироп', 180, 'images/Цезарь с креветками.jpg', 4),
    ('Мороженое с клубничным соусом', 140, 'Мороженое, клубничный соус', 100, 'images/Цезарь с креветками.jpg', 4)
    """

