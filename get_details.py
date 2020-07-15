def get_pub_details(results):

    pub_info = {}

    for craftBeerGood, craftBeerOkay, beerGardenY, beerGardenN, rooftopDeckY, rooftopDeckN, pokiesLots, pokiesLotsFew, pokiesNone, sportsBarY, sportsBarN, atmosphereTacky, atmosphereGrungy, atmosphereHip, atmosphereTrendy, animalPermittedY, animalPermittedN in results:

        craftBeer = False

        if craftBeerGood > craftBeerOkay:
            craftBeer = True

        beerGarden = False

        if beerGardenY > beerGardenN:
            beerGarden = True

        rooftopDeck = False

        if rooftopDeckY > rooftopDeckN:
            rooftopDeck = True

        pokies = 0
        pokies_numbers = pokiesLots

        if pokiesLots < pokiesLotsFew:
            pokies = 1
            pokies_numbers = pokiesLotsFew

        if pokies_numbers < pokiesNone:
            pokies = 2

        sportsBar = False

        if sportsBarY > sportsBarN:
            sportsBar = True

        atmosphere = 0
        atmosphereNumber = atmosphereTacky

        if atmosphereTacky < atmosphereGrungy:
            atmosphere = 1
            atmosphereNumber = atmosphereGrungy

        if atmosphereNumber < atmosphereHip:
            atmosphereHip = 2
            atmosphereNumber = atmosphereHip

        if atmosphereNumber < atmosphereTrendy:
            atmosphere = 3

        animalPermitted = False

        if animalPermittedY > animalPermittedN:
            animalPermitted = True

        pub_info = {
            "Craft_Beer": craftBeer,
            "Beer_Garden": beerGarden,
            "roof_top_deck": rooftopDeck,
            "pokies": pokies,
            "sports_bar": sportsBar,
            "atmosphere": atmosphere,
            "animal_permitted": animalPermitted
        }
    return pub_info

def get_cafe_details(results):

    cafe_info = {}

    for coffeeGood, coffeeOkay, coffeeBad, teaStrong, teaGood, teaBad, teaPotBig, teaPotSmall, teaPotCup, sugarGood, sugarBad, keepCupDiscountY, keepCupDiscountN in results:

        coffee = 0
        _coffee = coffeeGood

        if coffeeGood < coffeeOkay:
            coffee = 1
            _coffee = coffeeOkay

        if _coffee < coffeeBad:
            coffee = 2

        tea = 0
        _tea = teaStrong

        if teaStrong < teaGood:
            tea = 1
            _tea = teaGood

        if _tea < teaBad:
            tea = 2

        teaPot = 0
        _teaPot = teaPotBig

        if teaPotBig < teaPotSmall:
            teaPot = 1
            _teaPot = teaPotSmall

        if _teaPot < teaPotCup:
            teaPot = 2

        sugar = False

        if sugarGood > sugarBad:
            sugar = True

        keepCup = False

        if keepCupDiscountY > keepCupDiscountN:
            keepCup = True

        cafe_info = {
            "coffee": coffee,
            "tea": tea,
            "tea_pot": teaPot,
            "sugar": sugar,
            "keep_cup": keepCup
        }

    return cafe_info
