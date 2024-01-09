from .models import countModel
from rest_framework.response import Response
from rest_framework.views import APIView

class CountView(APIView):
	def get(self,request):
		try:
			count = countModel.objects.count()
			return Response({'count':count},status=200)
		except Exception as e:
			return Response({'error':str(e)},status=400)