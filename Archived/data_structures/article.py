class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'get_absolute_url']

    stocks = [
        ('GOOG', 'Google'),
        ('T', 'AT&T'), 
        ('AAPL', 'Apple'),
    ] 

    def memorize(func): 
        cache = {} 
        def innerFunc(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return innerFunc 


