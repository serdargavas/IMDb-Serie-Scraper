import scrapy


class SerieSpider(scrapy.Spider):
    name = 'serie'
    allowed_domains = ['imdb.com','youtube.com']
    start_urls = ['https://www.imdb.com/search/title/?title_type=tv_series&release_date=,2022-03-10&start=0&ref_=adv_nxt']

    def parse(self, response):
        for link in response.css('div.lister-item div.lister-item-image a::attr(href)'):
            yield response.follow(link.get(), callback=self.id_scrape)

        next_page = response.css('a.lister-page-next.next-page::attr("href")').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def id_scrape(self, response):
        data = {}
        data['id'] = response.url.replace('/?ref_=adv_li_tt', '').replace('https://www.imdb.com/title/', '').replace(
            '/', '')
        data['type'] = "Serie"
        data['year'] = response.css(
            'ul[data-testid=hero-title-block__metadata] li:nth-child(2) a::text').extract_first()
        release_date = response.css('li[data-testid=title-details-releasedate] div ul li a::text').extract_first()
        split_date = release_date.split(" ")[:-1]
        if len(split_date) == 1:
            year = split_date[0]
            combined_date = year.__add__("-01-01")
        elif len(split_date) == 2:
            year = split_date[1]
            month = split_date[0]
            if (month == "January"):
                month = "01"
            elif (month == "February"):
                month = "02"
            elif (month == "March"):
                month = "03"
            elif (month == "April"):
                month = "04"
            elif (month == "May"):
                month = "05"
            elif (month == "June"):
                month = "06"
            elif (month == "July"):
                month = "07"
            elif (month == "August"):
                month = "08"
            elif (month == "September"):
                month = "09"
            elif (month == "October"):
                month = "10"
            elif (month == "November"):
                month = "11"
            elif (month == "December"):
                month = "12"
            combined_date = year.__add__("-") + month.__add__("-01")
        else:
            year = split_date[2]
            month = split_date[0]
            day = split_date[1].replace(',', '')
            if (int(day) < 10):
                day = "0" + day
            if (month == "January"):
                month = "01"
            elif (month == "February"):
                month = "02"
            elif (month == "March"):
                month = "03"
            elif (month == "April"):
                month = "04"
            elif (month == "May"):
                month = "05"
            elif (month == "June"):
                month = "06"
            elif (month == "July"):
                month = "07"
            elif (month == "August"):
                month = "08"
            elif (month == "September"):
                month = "09"
            elif (month == "October"):
                month = "10"
            elif (month == "November"):
                month = "11"
            elif (month == "December"):
                month = "12"
            combined_date = year.__add__("-") + month.__add__("-") + day
        data['releaseDate'] = combined_date
        data['title'] = response.css('h1[data-testid=hero-title-block__title]::text').get()
        data['fullTitle'] = data['title'] + " (" + data['year'] + ")"
        data['image'] = response.css('img.ipc-image::attr(src)').get().replace('190', '380').replace('281', '562')
        data['plot'] = response.css('div[data-testid=storyline-plot-summary] div div::text').extract_first()
        data['plot_short'] = response.css('span[data-testid=plot-xl]::text').extract_first()
        runtime = response.css('li[data-testid=title-techspec_runtime] div::text').extract()
        data['runtimeStr'] = ''.join(runtime)
        directors = response.css(
            'section[data-testid=title-cast] ul li:nth-child(1) div ul li a::text').extract()
        data['directors'] = [director.strip() for director in directors]
        writers = response.css(
            'section[data-testid=title-cast] ul li:nth-child(2) div ul li a::text').extract()
        data['writers'] = [writer.strip() for writer in writers]
        stars = response.css(
            'div[data-testid=title-pc-wide-screen] li[data-testid=title-pc-principal-credit]:last-child div ul li a::text').extract()
        data['stars'] = stars
        data['creator'] = response.css('section[data-testid=title-cast] ul li div ul li a::text').extract_first()
        data['companies'] = response.css('li[data-testid=title-details-companies] div ul li a::text').extract()
        data['countries'] = response.css('li[data-testid=title-details-origin] div ul li a::text').extract()
        data['genres'] = response.css('li[data-testid=storyline-genres] div ul li a::text').extract()
        data['imDbRating'] = float(response.css('div[data-testid=hero-rating-bar__aggregate-rating__score] span::text').extract_first())
        data['tagline'] = response.css('li[data-testid=storyline-taglines] div div ul li span::text').extract_first()
        data['actors'] = []
        actors = response.css(
            'div[data-testid=title-cast-item]')
        for actor in actors:
            item = {}
            image = actor.xpath('div[1]/div/div/img/@src').get()
            if image:
                item['image'] = image.replace('140_CR', '280_CR').replace('140,140', '280,280')
            item['name'] = actor.css('a[data-testid=title-cast-item__actor]::text').extract_first()
            item['asCharacter'] = actor.css('span[data-testid=cast-item-characters-with-as]::text').extract_first()
            item['episodes'] = actor.css('span[data-testid=title-cast-item__episodes]::text').extract_first()
            data['actors'].append(item)
        keywordList = response.css('div[data-testid=storyline-plot-keywords] a span::text').extract()
        if keywordList:
            data['keywordList'] = keywordList[:-1]
        data['languages'] = response.css('li[data-testid=title-details-languages] div ul li a::text').extract()
        data['similars'] = []
        similars = response.css(
            'section[data-testid=MoreLikeThis] div.ipc-shoveler div.ipc-sub-grid div.ipc-poster-card')
        for similar in similars:
            similar_item = {}
            split_similar_item = similar.xpath('div[1]/a/@href').get().replace(
                '/title/', '').split("/")
            similar_item['id'] = split_similar_item[0]
            data['similars'].append(similar_item)
        data['images'] = []
        images = response.css('section[data-testid=Photos] div[data-testid=shoveler] div div img::attr(src)').extract()
        for image in images:
            image_item = {}
            split_image = image.split("._")
            image_item['url'] = split_image[0].__add__("._V1_FMjpg_UX1280_.jpg")
            data['images'].append(image_item)
        video = response.css('div[data-testid=hero-media__slate] a::attr(href)').get()
        if video:
            split_video = video.split("?")
            data['video'] = "https://www.imdb.com/video/imdb/".__add__(split_video[0].replace('/video/', '')).__add__(
                "/imdb/embed")
        episode_url = response.css('div[data-testid=episodes-header] a::attr(href)').get()
        data['episode_count'] = response.css(
            'div[data-testid=episodes-header] a h3 span.ipc-title__subtext::text').get()
        data['episodes'] = []
        request = scrapy.Request(url=response.urljoin(episode_url), callback=self.episode)
        request.cb_kwargs['data'] = data  # add more arguments for the callback
        yield request

    def episode(self, response, data):
        data = data
        serie = {}
        serie['episodes'] = []
        episodes = response.css('div.list_item')
        season_number = response.css('h3[id=episode_top]::text').extract_first().replace(u'\xa0', u' ')
        for episode in episodes:
            episode_number = episode.css('div.info meta::attr(content)').extract_first()
            image = episode.css('div.image img::attr(src)').extract_first()
            episode_info = episode.css('div.image div.hover-over-image div::text').extract_first()
            title = episode.css('div.info strong a::text').extract_first()
            date = episode.css('div.info div.airdate::text').extract_first()
            rating = episode.css(
                'div.info div.ipl-rating-widget div span.ipl-rating-star__rating::text').extract_first()
            if rating:
                rating = float(rating)
            plot = episode.css('div.info div.item_description::text').extract_first()
            item = {
                'episode_number': int(episode_number),
                'image': image,
                'episode_info': episode_info,
                'title': title,
                'date': date.strip(),
                'rating': rating,
                'plot': plot.strip()
            }
            serie['episodes'].append(item)
        data['episodes'].append({'season': season_number,'episodes': serie['episodes']})

        next_page = response.css('a[id=load_previous_episodes]::attr("href")').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            request = scrapy.Request(url=next_page, callback=self.episode)
            request.cb_kwargs['data'] = data
            yield request
        else:
            yield data




class SerieSingleSpider(scrapy.Spider):
    name = 'serie_single'
    allowed_domains = ['imdb.com','www.youtube.com']
    start_urls = ['https://www.imdb.com/title/tt11280740/?ref_=adv_li_tt']

    def parse(self, response):
        data = {}
        data['id'] = response.url.replace('/?ref_=adv_li_tt', '').replace('https://www.imdb.com/title/', '').replace(
            '/', '')
        data['type'] = "Serie"
        data['year'] = response.css(
            'ul[data-testid=hero-title-block__metadata] li:nth-child(2) a::text').extract_first()
        release_date = response.css('li[data-testid=title-details-releasedate] div ul li a::text').extract_first()
        split_date = release_date.split(" ")[:-1]
        if len(split_date) == 1:
            year = split_date[0]
            combined_date = year.__add__("-01-01")
        elif len(split_date) == 2:
            year = split_date[1]
            month = split_date[0]
            if (month == "January"):
                month = "01"
            elif (month == "February"):
                month = "02"
            elif (month == "March"):
                month = "03"
            elif (month == "April"):
                month = "04"
            elif (month == "May"):
                month = "05"
            elif (month == "June"):
                month = "06"
            elif (month == "July"):
                month = "07"
            elif (month == "August"):
                month = "08"
            elif (month == "September"):
                month = "09"
            elif (month == "October"):
                month = "10"
            elif (month == "November"):
                month = "11"
            elif (month == "December"):
                month = "12"
            combined_date = year.__add__("-") + month.__add__("-01")
        else:
            year = split_date[2]
            month = split_date[0]
            day = split_date[1].replace(',', '')
            if (int(day) < 10):
                day = "0" + day
            if (month == "January"):
                month = "01"
            elif (month == "February"):
                month = "02"
            elif (month == "March"):
                month = "03"
            elif (month == "April"):
                month = "04"
            elif (month == "May"):
                month = "05"
            elif (month == "June"):
                month = "06"
            elif (month == "July"):
                month = "07"
            elif (month == "August"):
                month = "08"
            elif (month == "September"):
                month = "09"
            elif (month == "October"):
                month = "10"
            elif (month == "November"):
                month = "11"
            elif (month == "December"):
                month = "12"
            combined_date = year.__add__("-") + month.__add__("-") + day
        data['releaseDate'] = combined_date
        data['title'] = response.css('h1[data-testid=hero-title-block__title]::text').get()
        data['fullTitle'] = data['title'] + " (" + data['year'] + ")"
        data['image'] = response.css('img.ipc-image::attr(src)').get().replace('190', '380').replace('281', '562')
        data['plot'] = response.css('div[data-testid=storyline-plot-summary] div div::text').extract_first()
        data['plot_short'] = response.css('span[data-testid=plot-xl]::text').extract_first()
        runtime = response.css('li[data-testid=title-techspec_runtime] div::text').extract()
        data['runtimeStr'] = ''.join(runtime)
        directors = response.css(
            'section[data-testid=title-cast] ul li:nth-child(1) div ul li a::text').extract()
        data['directors'] = [director.strip() for director in directors]
        writers = response.css(
            'section[data-testid=title-cast] ul li:nth-child(2) div ul li a::text').extract()
        data['writers'] = [writer.strip() for writer in writers]
        stars = response.css(
            'div[data-testid=title-pc-wide-screen] li[data-testid=title-pc-principal-credit]:last-child div ul li a::text').extract()
        data['stars'] = stars
        data['creator'] = response.css('section[data-testid=title-cast] ul li div ul li a::text').extract_first()
        data['companies'] = response.css('li[data-testid=title-details-companies] div ul li a::text').extract()
        data['countries'] = response.css('li[data-testid=title-details-origin] div ul li a::text').extract()
        data['genres'] = response.css('li[data-testid=storyline-genres] div ul li a::text').extract()
        data['imDbRating'] = float(
            response.css('div[data-testid=hero-rating-bar__aggregate-rating__score] span::text').extract_first())
        data['tagline'] = response.css('li[data-testid=storyline-taglines] div div ul li span::text').extract_first()
        data['actors'] = []
        actors = response.css(
            'div[data-testid=title-cast-item]')
        for actor in actors:
            item = {}
            image = actor.xpath('div[1]/div/div/img/@src').get()
            if image:
                item['image'] = image.replace('140_CR', '280_CR').replace('140,140', '280,280')
            item['name'] = actor.css('a[data-testid=title-cast-item__actor]::text').extract_first()
            item['asCharacter'] = actor.css('span[data-testid=cast-item-characters-with-as]::text').extract_first()
            item['episodes'] = actor.css('span[data-testid=title-cast-item__episodes]::text').extract_first()
            data['actors'].append(item)
        keywordList = response.css('div[data-testid=storyline-plot-keywords] a span::text').extract()
        if keywordList:
            data['keywordList'] = keywordList[:-1]
        data['languages'] = response.css('li[data-testid=title-details-languages] div ul li a::text').extract()
        data['similars'] = []
        similars = response.css(
            'section[data-testid=MoreLikeThis] div.ipc-shoveler div.ipc-sub-grid div.ipc-poster-card')
        for similar in similars:
            similar_item = {}
            split_similar_item = similar.xpath('div[1]/a/@href').get().replace(
                '/title/', '').split("/")
            similar_item['id'] = split_similar_item[0]
            data['similars'].append(similar_item)
        data['images'] = []
        images = response.css('section[data-testid=Photos] div[data-testid=shoveler] div div img::attr(src)').extract()
        for image in images:
            image_item = {}
            split_image = image.split("._")
            image_item['url'] = split_image[0].__add__("._V1_FMjpg_UX1280_.jpg")
            data['images'].append(image_item)
        video = response.css('div[data-testid=hero-media__slate] a::attr(href)').get()
        if video:
            split_video = video.split("?")
            data['video'] = "https://www.imdb.com/video/imdb/".__add__(split_video[0].replace('/video/', '')).__add__(
                "/imdb/embed")
        episode_url = response.css('div[data-testid=episodes-header] a::attr(href)').get()
        data['episode_count'] = response.css(
            'div[data-testid=episodes-header] a h3 span.ipc-title__subtext::text').get()
        data['episodes'] = []
        request = scrapy.Request(url=response.urljoin(episode_url), callback=self.episode)
        request.cb_kwargs['data'] = data  # add more arguments for the callback
        yield request

    def episode(self, response, data):
        data = data
        serie = {}
        serie['episodes'] = []
        episodes = response.css('div.list_item')
        season_number = response.css('h3[id=episode_top]::text').extract_first().replace(u'\xa0', u' ')
        for episode in episodes:
            episode_number = episode.css('div.info meta::attr(content)').extract_first()
            image = episode.css('div.image img::attr(src)').extract_first()
            episode_info = episode.css('div.image div.hover-over-image div::text').extract_first()
            title = episode.css('div.info strong a::text').extract_first()
            date = episode.css('div.info div.airdate::text').extract_first()
            rating = episode.css(
                'div.info div.ipl-rating-widget div span.ipl-rating-star__rating::text').extract_first()
            if rating:
                rating = float(rating)
            plot = episode.css('div.info div.item_description::text').extract_first()
            item = {
                'episode_number': int(episode_number),
                'image': image,
                'episode_info': episode_info,
                'title': title,
                'date': date.strip(),
                'rating': rating,
                'plot': plot.strip()
            }
            serie['episodes'].append(item)
        data['episodes'].append({'season': season_number, 'episodes': serie['episodes']})

        next_page = response.css('a[id=load_previous_episodes]::attr("href")').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            request = scrapy.Request(url=next_page, callback=self.episode)
            request.cb_kwargs['data'] = data
            yield request
        else:
            yield data




