from gazette.spiders.base import FecamGazetteSpider


class ScVideiraSpider(FecamGazetteSpider):
    name = "sc_videira"
    FECAM_QUERY = "cod_entidade:290"
    TERRITORY_ID = "4219309"
