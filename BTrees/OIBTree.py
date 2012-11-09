##############################################################################
#
# Copyright (c) 2001-2012 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

__all__ = ('Bucket', 'Set', 'BTree', 'TreeSet',
           'OIBucket', 'OISet', 'OIBTree', 'OITreeSet',
           'union', 'intersection', 'difference',  
           'weightedUnion', 'weightedIntersection',
          )

from zope.interface import moduleProvides

from BTrees.Interfaces import IObjectIntegerBTreeModule
from BTrees.___BTree import Bucket
from BTrees.___BTree import MERGE
from BTrees.___BTree import MERGE_WEIGHT_numeric
from BTrees.___BTree import MERGE_DEFAULT_float
from BTrees.___BTree import Set
from BTrees.___BTree import Tree as BTree
from BTrees.___BTree import TreeSet
from BTrees.___BTree import difference as _difference
from BTrees.___BTree import intersection as _intersection
from BTrees.___BTree import setop as _setop
from BTrees.___BTree import to_ob as _to_key
from BTrees.___BTree import to_int as _to_value
from BTrees.___BTree import union as _union
from BTrees.___BTree import weightedIntersection as _weightedIntersection
from BTrees.___BTree import weightedUnion as _weightedUnion

_BUCKET_SIZE = 60
_TREE_SIZE = 250
using64bits = True

class OIBucketPy(Bucket):
    MAX_SIZE = _BUCKET_SIZE
    _to_key = _to_key
    _to_value = _to_value
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


class OISetPy(Set):
    MAX_SIZE = _BUCKET_SIZE
    _to_key = _to_key
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


class OIBTreePy(BTree):
    MAX_SIZE = _TREE_SIZE
    _to_key = _to_key
    _to_value = _to_value
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


class OITreeSetPy(TreeSet):
    MAX_SIZE = _TREE_SIZE
    _to_key = _to_key
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


# Can't declare forward refs, so fix up afterwards:

OIBucketPy._mapping_type = OIBucketPy._bucket_type = OIBucketPy
OIBucketPy._set_type = OISetPy

OISetPy._mapping_type = OIBucketPy
OISetPy._set_type = OISetPy._bucket_type = OISetPy

OIBTreePy._mapping_type = OIBTreePy._bucket_type = OIBucketPy
OIBTreePy._set_type = OISetPy

OITreeSetPy._mapping_type = OIBucketPy
OITreeSetPy._set_type = OITreeSetPy._bucket_type = OISetPy


differencePy = _setop(_difference, OISetPy)
unionPy = _setop(_union, OISetPy)
intersectionPy = _setop(_intersection, OISetPy)
weightedUnionPy = _setop(_weightedUnion, OISetPy)
weightedIntersectionPy = _setop(_weightedIntersection, OISetPy)

try:
    from _OIBTree import OIBucket
    from _OIBTree import OISet
    from _OIBTree import OIBTree
    from _OIBTree import OITreeSet
    from _OIBTree import difference
    from _OIBTree import union
    from _OIBTree import intersection
    from _OIBTree import weightedUnion
    from _OIBTree import weightedIntersection
except ImportError: #pragma NO COVER
    OIBucket = OIBucketPy
    OISet = OISetPy
    OIBTree = OIBTreePy
    OITreeSet = OITreeSetPy
    difference = differencePy
    union = unionPy
    intersection = intersectionPy
    weightedUnion = weightedUnionPy
    weightedIntersection = weightedIntersectionPy


Bucket = OIBucket
Set = OISet
BTree = OIBTree
TreeSet = OITreeSet

moduleProvides(IObjectIntegerBTreeModule)
