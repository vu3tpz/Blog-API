from viewflow.fsm import State
from viewflow.workflow import flow

from apps.blog.config import BlogStatusChoices

# class BlogWorkflow(flow.Flow):

#     draft = flow.Start()

# draft = Draft().next(Review)
# review = Review().next(Publish).next(Withheld).next(Reject)
# withheld = Withheld().next(Appeal)
# publish = Publish()
# appeal = Appeal().next(Review)
# reject = Reject()
