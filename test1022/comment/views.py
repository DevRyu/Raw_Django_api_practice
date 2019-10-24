import json
from django.views import View
from django.http  import JsonResponse
from .models      import Comments


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            comment_writer = data['comment_writer'],
            comment_text =data['comment_text']
        ).save()
        return JsonResponse({"message":"SUCCESS"},status=200)

    def get(self, request):
        # 방법1 코멘트의 값들만
        commentss = list(Comments.objects.values())
        print(commentss)
        # 방법2 리스트 생성
        comment_list = []
        # 코멘트의 객체 다가져옴
        comments = Comments.objects.all()
        for comment in comments:
            print (comment)
            comment_list.append({
                "아이디"      : comment.id,
                "이름"    : comment.comment_writer,
                "댓글내용" : comment.comment_text,
                "게시일자"  : comment.registered_date,
            })
        print(comment_list)

            
        return JsonResponse({"data":comment_list}, status=200)

