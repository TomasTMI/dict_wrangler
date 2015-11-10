# Object module: comment.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'comment'


# Comment Object - (Inherited from SuperObj)
class CommentObj(obj.SuperObj):
    def __init__(self):
        # Attributes: father, children, ...
        super(CommentObj, self).__init__()
        self.value = None

    def setValue(self, value):
        self.value = value

    def __repr__(self):
        return "comment"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        # Object
        data = dictionary['value']
        Comment_O = CommentObj()
        Comment_O.setValue(data)
        Comment_O.setParent(objecte)
        results.append(Comment_O)

        # Next element
        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, Comment_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, Comment_O)
    return
