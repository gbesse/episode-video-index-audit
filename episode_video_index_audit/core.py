import math
from .common import number,integer,identifier,unique_ids
def run(d):
 videos=d['videos'];episodes=d['episodes'];unique_ids(videos);unique_ids(episodes)
 if len(videos)+len(episodes)>10000:raise ValueError('size')
 byid={v['id']:v for v in videos}
 for v in videos:number(v['duration'],0);integer(v['frames'],0)
 out=[]
 for e in episodes:
  start=number(e['from_time'],0);end=number(e['to_time'],0)
  if end<start:raise ValueError('time_order')
  vid=byid.get(e['video_id']);reasons=[]
  if not vid:reasons.append('missing_video')
  elif end>vid['duration']:reasons.append('time_beyond_duration')
  if vid and'frame_from'in e:
   lo=integer(e['frame_from'],0);hi=integer(e['frame_to'],lo)
   if hi>vid['frames']:reasons.append('frame_beyond_count')
  alternatives=[v['id']for v in videos if end<=v['duration']and v['id']!=e['video_id']]
  out.append(dict(id=e['id'],video_id=e['video_id'],status='invalid'if reasons else 'within_declared_bounds',reasons=reasons,possible_length_only_alternatives=alternatives if reasons else []))
 return dict(episodes=out,invalid=sum(x['status']=='invalid'for x in out),convention='time_end_inclusive_limit_frame_end_exclusive')
