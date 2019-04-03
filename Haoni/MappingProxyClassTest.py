#_*_utf8_*_
'''
ONLY FOR TEST!
ONLY FOR TEST!
'''
from types import MappingProxyType    # Use module `type`


class Students:
    def __init__(self, name=None):
        try:
            self.name = name
            self.info = None
            #    inner attr
            self._info = None
            #    outter attr
            self._none = True
        except Exception as e:
            self._none = False
            print(e)

    def setinfo(self, obj):
        if self._none:
            try:
                self.info = obj
                self._info = MappingProxyType(obj)
            except json.JSONDecodeError:
                self._none = True

    def __call__(self):
        if self._none:
            try:
                return self._info
            except TypeError:
                if self._info:
                    return self._info
            except NameError:
                return None


def demo():
    a_record = dict(score='A', name='John', birthday='2019/01/02')
    a_student = Students()
    a_student.setinfo(a_record)
    # Now it's time to show the intersection of student_a
    a_map_obj = a_student()
    print(type(a_map_obj))
    for i in a_student.info.keys():
        print("%s => %s" % (i, a_map_obj[i]))


if __name__ == '__main__':
    demo()
