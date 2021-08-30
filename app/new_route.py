from _typeshed import IdentityFunction
from app.routes_new import add_film_to_filmography
from typing import cast


def get_actor(actor_name):
    is actor in DB?
        does actor have name, id, image_url, filmography?
            for film in filmography:
                is film complete?
                    get featured_cast






                    actor
                        name
                        id
                        image
                        filmography

                        for film in filmography
                            if it doesn't exist in db
                                create film
                                    title
                                    id
                                    image
                                    
                                    add featured_cast
                                    add actor to cast

                            if it does exist in db,
                                does it have actor in cast?
                                    nothing or add
                                does it have featured cast?
                                    nothing or add featured cast


                        add featured cast
                            get movie Info

