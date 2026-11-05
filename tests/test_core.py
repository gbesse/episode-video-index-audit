import unittest,math
from episode_video_index_audit.core import run
class DomainTests(unittest.TestCase):
 def test_wrong_video(self):
  x=run({'videos':[dict(id='a',duration=1,frames=30),dict(id='b',duration=5,frames=150)],'episodes':[dict(id='e',video_id='a',from_time=2,to_time=3)]})['episodes'][0];self.assertEqual(x['reasons'],['time_beyond_duration']);self.assertEqual(x['possible_length_only_alternatives'],['b'])
 def test_boundary(self):
  self.assertEqual(run({'videos':[dict(id='a',duration=1,frames=30)],'episodes':[dict(id='e',video_id='a',from_time=0,to_time=1,frame_from=0,frame_to=30)]})['invalid'],0)
 def test_missing(self):self.assertEqual(run({'videos':[],'episodes':[dict(id='e',video_id='x',from_time=0,to_time=1)]})['invalid'],1)
