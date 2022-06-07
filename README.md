# IMDB Serie Scraper

Scrape IMDb Series with my code

## Description

Scraping using Python Scrapy with simple steps. Output format is JSON.

## Getting Started

### Dependencies

- Scrapy

### Installing

- Download zip file

### Executing program

- Install dependencies
- Create virtual enviroment
- Go into spiders folder in terminal

- To get all series, write 'scrapy crawl serie -O serie.json'
- To get single serie, change the url in code and then write 'scrapy crawl serie_single -O serie-single.json'

### Output format

```
{
        "id": "tt13668894",
        "type": "Serie",
        "year": "2021\u2013 ",
        "releaseDate": "2021-12-29",
        "title": "The Book of Boba Fett",
        "fullTitle": "The Book of Boba Fett (2021\u2013 )",
        "image": "https://m.media-amazon.com/images/M/MV5BZjllZjE1MWEtYTJhZC00MWIyLTliMjEtYzM3ODc4YzQ2MjFlXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_QL75_UX380_CR0,0,380,562_.jpg",
        "plot": "The legendary bounty hunter Boba Fett navigates the underworld of the galaxy with mercenary Fennec Shand when they return to the sands of Tatooine to stake their claim on the territory formerly ruled by the deceased crime lord Jabba the Hutt.",
        "plot_short": "Bounty hunter Boba Fett & mercenary Fennec Shand navigate the underworld when they return to Tatooine to claim Jabba the Hutt's old turf.",
        "runtimeStr": "38 minutes",
        "directors": [
            "Jon Favreau"
        ],
        "writers": [],
        "stars": [
            "Temuera Morrison",
            "Ming-Na Wen",
            "Frank Trigg"
        ],
        "creator": "Jon Favreau",
        "companies": [
            "Golem Creations",
            "Lucasfilm"
        ],
        "countries": [
            "United States"
        ],
        "genres": [
            "Action",
            "Adventure",
            "Sci-Fi"
        ],
        "imDbRating": 7.5,
        "tagline": null,
        "actors": [
            {
                "image": "https://m.media-amazon.com/images/M/MV5BNmRlZWQxMjUtNjJkZS00MTY2LWJlYzgtN2Y3N2VhYTUwZDM4XkEyXkFqcGdeQXVyMTIzMDI5MzAy._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Temuera Morrison",
                "asCharacter": "as Boba Fett",
                "episodes": "7 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMTIyNjUwNTk3OV5BMl5BanBnXkFtZTcwOTE4NTMzMQ@@._V1_QL75_UX280_CR0,0,280,280_.jpg",
                "name": "Ming-Na Wen",
                "asCharacter": "as Fennec Shand",
                "episodes": "7 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMzg3YWYxMTItMTQxNS00NDNhLTlkZTYtNzI0OTY4MDIzOWY3XkEyXkFqcGdeQXVyMjI0NzcxNTQ@._V1_QL75_UX280_CR0,1,280,280_.jpg",
                "name": "Frank Trigg",
                "asCharacter": "as Gamorrean Guard",
                "episodes": "6 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BM2U1YzdlZTYtZmE0MS00NjZiLWIyOTUtZWEzNmE3M2QzY2M1XkEyXkFqcGdeQXVyMTkzNzQ0NDY@._V1_QL75_UX280_CR0,0,280,280_.jpg",
                "name": "Collin Hymes",
                "asCharacter": "as Gamorrean Guard",
                "episodes": "6 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BZmFiY2VjZjEtNjdhNi00NmNkLWFiMmEtZDY0NjZkNDg0NGNmXkEyXkFqcGdeQXVyMTI1Nzk0MzM1._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Leilani Shiu",
                "asCharacter": "as Jawa",
                "episodes": "6 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMTgzMjQ0NTc5Nl5BMl5BanBnXkFtZTcwMDc0MDYwOA@@._V1_QL75_UX280_CR0,11,280,280_.jpg",
                "name": "Matt Berry",
                "asCharacter": "as 8D8",
                "episodes": "5 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMTEwMzkyNzU2NDleQTJeQWpwZ15BbWU4MDc0MTM1NDgx._V1_QL75_UY280_CR35,0,280,280_.jpg",
                "name": "David Pasquesi",
                "asCharacter": "as Mok Shaiz's Majordomo",
                "episodes": "5 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BNzlkMWVmMTQtMTQ1Yi00YzE4LWIyNmQtMWYyYTEwNzcxNDY0XkEyXkFqcGdeQXVyMTk5OTgyODM@._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Carey Jones",
                "asCharacter": "as Black Krrsantan",
                "episodes": "5 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMTc1MTg4MDAyN15BMl5BanBnXkFtZTcwNDgwNTExMw@@._V1_QL75_UX280_CR0,1,280,280_.jpg",
                "name": "Jennifer Beals",
                "asCharacter": "as Garsa Fwip",
                "episodes": "4 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMTc0NDg4ODAwNF5BMl5BanBnXkFtZTgwMTIxNTA0MjE@._V1_QL75_UX280_CR0,15,280,280_.jpg",
                "name": "Robert Rodriguez",
                "asCharacter": "as Dokk Strassi",
                "episodes": "4 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BODMyYThhNGEtNWJkYy00YjU1LWJmZTAtMTY5ZGQ5ODIzOGEwXkEyXkFqcGdeQXVyNjUxMjc1OTM@._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Marlon Aquino",
                "asCharacter": "as Twi'lek Server",
                "episodes": "4 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMzUyNzgwYjYtMWM4OS00N2EyLThiMTUtMzdlMTBiODMyM2EyXkEyXkFqcGdeQXVyMTQyOTk2ODcx._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Andrea Bartlow",
                "asCharacter": "as Twi'lek Server",
                "episodes": "4 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BYzQ5Yzg1NzktMDcxNC00ZDc1LWJlMjEtNTg2ZjRlOTk4ZDNjXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_QL75_UX280_CR0,6,280,280_.jpg",
                "name": "Pedro Pascal",
                "asCharacter": "as The Mandalorian",
                "episodes": "3 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BOTk5YTk5NGUtMzhkNC00NTk5LTliN2EtOWNhMzc3N2U5NWI3XkEyXkFqcGdeQXVyMTExNzQzMDE0._V1_QL75_UX280_CR0,0,280,280_.jpg",
                "name": "Sophie Thatcher",
                "asCharacter": "as Drash",
                "episodes": "3 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BYjE2NzJlZjQtMWUzNy00ZDNjLWIyODAtOWRkOWQ4MThlNGY1XkEyXkFqcGdeQXVyMTUxNzU2OQ@@._V1_QL75_UX280_CR0,20,280,280_.jpg",
                "name": "Jordan Bolger",
                "asCharacter": "as Skad",
                "episodes": "3 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BOWYwOTc4ZTktNmQyMS00YTk2LTgwYWEtMTA1ZGIyZDNmNTg2XkEyXkFqcGdeQXVyMjQxMDAzODY@._V1_QL75_UX280_CR0,0,280,280_.jpg",
                "name": "Joanna Bennett",
                "asCharacter": "as Tusken Warrior",
                "episodes": "3 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BMTU5MTIxNTUwN15BMl5BanBnXkFtZTgwMzkyNjk2ODE@._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Barry Lowin",
                "asCharacter": "as Garfalaquox",
                "episodes": "3 episodes"
            },
            {
                "image": "https://m.media-amazon.com/images/M/MV5BYTJkMGZiZTEtOTRhNC00YjQxLTk0YzgtMmQzNzRhYmMzNTA1XkEyXkFqcGdeQXVyNzY1MzIyNTA@._V1_QL75_UX280_CR0,12,280,280_.jpg",
                "name": "Xavier Jimenez",
                "asCharacter": "as Tusken Chief",
                "episodes": "3 episodes"
            }
        ],
        "keywordList": [
            "star wars",
            "spin off",
            "space western",
            "sci fi western",
            "gunfighter"
        ],
        "languages": [
            "English"
        ],
        "similars": [
            {
                "id": "tt8111088"
            },
            {
                "id": "tt13146488"
            },
            {
                "id": "tt10160804"
            },
            {
                "id": "tt9288030"
            },
            {
                "id": "tt12708542"
            },
            {
                "id": "tt0458290"
            },
            {
                "id": "tt10392648"
            },
            {
                "id": "tt9032400"
            },
            {
                "id": "tt9140554"
            },
            {
                "id": "tt7161856"
            },
            {
                "id": "tt1190634"
            },
            {
                "id": "tt0121766"
            }
        ],
        "images": [
            {
                "url": "https://m.media-amazon.com/images/M/MV5BZGM0MGJiNzYtOGJkMC00YTQxLWFjZmItYWIwYjdlNDkzZTJhXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BMTc3Nzk3NTUtZDRmMC00NTliLThiNjUtMTNlOTFlMTFjYzc2XkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BYTIwMDdmOTktMGRjZC00YzZkLWFhODItOGFjOTBjYTljZGNlXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BZGM3YzhjYmUtOTE5Zi00ODhiLTkyMTktMDJiMzJiNmU2ODVkXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BYzA3NDIwODctNjAwMS00YTA3LTg0OTctMzMyYWRjN2UwZGIyXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BNTY1NzI4OWQtNzY4OS00ZmE5LTkyMjctNmIzNTUxN2JiYTM4XkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BNzA3NmJkMzItYWU2NS00NTllLTkyZDItNTI1MWU1MDg2YTEyXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BOTA0YzFjM2QtMDdkNS00ZDc2LWFmZWItZDE2ZmU0MmQ4Mzg4XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BOWVhOGIwODYtYzA1ZC00MGFkLTk4MGEtZjUzM2ZkMmI4YzA0XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BZmE1Nzk5MGItNDE4My00MGU2LWFkNzEtYjlmZDM2YWMwNzE1XkEyXkFqcGdeQXVyMTAyOTE2ODg0._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BOTg1M2ZiZmQtYWM2MS00MDUyLWFhNjEtYTkzNGM2N2MyOTc0XkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_FMjpg_UX1280_.jpg"
            },
            {
                "url": "https://m.media-amazon.com/images/M/MV5BMmQ3Y2MyMmItNjE2Yy00MDRmLWI1ZTItMzNjZTBiZTFiOTIyXkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_FMjpg_UX1280_.jpg"
            }
        ],
        "video": "https://www.imdb.com/video/imdb/vi3711222553/imdb/embed",
        "episode_count": "7",
        "episodes": [
            {
                "season": "Season 1",
                "episodes": [
                    {
                        "episode_number": 1,
                        "image": "https://m.media-amazon.com/images/M/MV5BZThkYjdmNmQtZDVjNS00YzBiLThkNGEtMzdlYzk3MDkyZGE4XkEyXkFqcGdeQXVyNTA4NzExMDg@._V1_UX224_CR0,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep1",
                        "title": "Chapter 1: Stranger in a Strange Land",
                        "date": "29 Dec. 2021",
                        "rating": 7.4,
                        "plot": "Boba holds court."
                    },
                    {
                        "episode_number": 2,
                        "image": "https://m.media-amazon.com/images/M/MV5BMGI3ZWY4ZDEtY2Y1YS00ZDBlLTg0NzktMDAwNzFiMmFjNmVjXkEyXkFqcGdeQXVyMTA4OTg1Mzc1._V1_UY126_CR35,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep2",
                        "title": "Chapter 2: The Tribes of Tatooine",
                        "date": "5 Jan. 2022",
                        "rating": 8.2,
                        "plot": "Boba faces new challengers on Tatooine."
                    },
                    {
                        "episode_number": 3,
                        "image": "https://m.media-amazon.com/images/M/MV5BOWE3MWEzNGYtNjQ1Yi00MzQzLWI5NjMtNDI0NmVlOWI0OWQ4XkEyXkFqcGdeQXVyNTA4NzExMDg@._V1_UX224_CR0,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep3",
                        "title": "Chapter 3: The Streets of Mos Espa",
                        "date": "12 Jan. 2022",
                        "rating": 6.4,
                        "plot": "Boba must deal with two very different threats."
                    },
                    {
                        "episode_number": 4,
                        "image": "https://m.media-amazon.com/images/M/MV5BNzA3MDBhYzgtZGI2NS00NTA5LWFhNGMtYjljMDA1YjlhNmIzXkEyXkFqcGdeQXVyNjczOTE0MzM@._V1_UX224_CR0,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep4",
                        "title": "Chapter 4: The Gathering Storm",
                        "date": "19 Jan. 2022",
                        "rating": 7.5,
                        "plot": "Boba partners with Fennec Shand."
                    },
                    {
                        "episode_number": 5,
                        "image": "https://m.media-amazon.com/images/M/MV5BODNlNDZlODUtNjVkZi00OGExLWI2OGMtZjE2NWM2OTczNjI3XkEyXkFqcGdeQXVyOTg3NjI1MTg@._V1_UY126_CR39,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep5",
                        "title": "Chapter 5: Return of the Mandalorian",
                        "date": "26 Jan. 2022",
                        "rating": 9.3,
                        "plot": "An unexpected ally emerges."
                    },
                    {
                        "episode_number": 6,
                        "image": "https://m.media-amazon.com/images/M/MV5BYmYyNTY5MzAtM2U4MS00NmQ1LWE5ZmUtNDZkMmFiOWZlZjlhXkEyXkFqcGdeQXVyNjczOTE0MzM@._V1_UY126_CR2,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep6",
                        "title": "Chapter 6: From the Desert Comes a Stranger",
                        "date": "2 Feb. 2022",
                        "rating": 9.4,
                        "plot": "Mysteries are explored and Boba Fett learns new information."
                    },
                    {
                        "episode_number": 7,
                        "image": "https://m.media-amazon.com/images/M/MV5BYjViNTQzM2ItZjJiMy00MGRkLWJmMDEtOTc2N2QwNzMwODYxXkEyXkFqcGdeQXVyNzA3NzIzMjk@._V1_UY126_CR36,0,224,126_AL_.jpg",
                        "episode_info": "S1, Ep7",
                        "title": "Chapter 7: In the Name of Honor",
                        "date": "9 Feb. 2022",
                        "rating": 7.7,
                        "plot": "Boba Fett and Fennec Shand face an escalating conflict."
                    }
                ]
            }
        ]
    }
```

## Help

You can message me for any issues. Keep that in mind imdb changin their structures too often that makes my code not work at all. Some of fields may require updates.

## Authors

@serdargavas
