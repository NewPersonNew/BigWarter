
import mmh3
from bitarray import bitarray


class BloomFilter(object):

    def __init__(self, bit_size):
        self.bit_size = bit_size
        self.bit_array = bitarray(bit_size)
        self.bit_array.setall(0)

    def add(self, url):
        # 添加一个url,同时将其hash成bitarray,然后把所有的位数变为1
        point_list = self.get_postions(url)
        for b in point_list:
            self.bit_array[b] = 1

    def contains(self, url):
        # 传入一个url,然后验证这个url是否存在集合中
        point_list = self.get_postions(url)
        result = True
        for b in point_list:
            result = result and self.bit_array[b]
        return result

    def get_postions(self, url):
        # 返回url经过hash之后的比特位数组
        point1 = mmh3.hash(url, 41) % self.bit_size  # 求取的是url经hash之后的数组跟bit_size的余数，保证我们的比特位索引小于bit_size
        point2 = mmh3.hash(url, 42) % self.bit_size
        point3 = mmh3.hash(url, 43) % self.bit_size
        point4 = mmh3.hash(url, 44) % self.bit_size
        point5 = mmh3.hash(url, 45) % self.bit_size
        point6 = mmh3.hash(url, 46) % self.bit_size
        point7 = mmh3.hash(url, 47) % self.bit_size
        return [point1, point2, point3, point4, point5, point6, point7]


if __name__ == '__main__':
    bloom = BloomFilter(50000)
    bloom.add('https://www.baidu.com')
    b = bloom.contains('https://www.baidu.com')
    c = bloom.contains('htttddddddd')
    print(b)
    print(c)
