

from scrapy_redis.dupefilter import RFPDupeFilter
from BloomFilter.py_bloomfilter import PyBloomFilter, conn


class BloomRFDupeFilter(RFPDupeFilter):

    def __init__(self, server, key, debug=False):
        """Initialize the duplicates filter.

        Parameters
        ----------
        server : redis.StrictRedis
            The redis server instance.
        key : str
            Redis key Where to store fingerprints.
        debug : bool, optional
            Whether to log filtered requests.

        """
        super().__init__(server, key, debug)
        self.server = server
        self.key = key
        self.debug = debug
        self.logdupes = True

        # 集成布隆过滤器
        self.bf = PyBloomFilter(conn=conn, key=key)  # 利用连接池连接Redis

    def request_seen(self, request):
        """Returns True if request was already seen.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        bool

        """
        fp = self.request_fingerprint(request)
        # This returns the number of values added, zero if already exists.
        # added = self.server.sadd(self.key, fp)
        # return added == 0

        # 集成布隆过滤器
        if self.bf.is_exist(fp):  # 判断如果域名在Redis里存在
            return True
        else:
            self.bf.add(fp)  # 如果不存在，将域名添加到Redis
            return False