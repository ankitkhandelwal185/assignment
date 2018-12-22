# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from college.models import College, Course
from .serializers import CollegeSerializer, CourseSerializer
# Create your views here.

class CollegeDetail(APIView):

    def post(self, request):
        data = request.data
        if isinstance(data, list):
            serializer = CollegeSerializer(data, many=True)
        else:
            serializer = CollegeSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, college_id):
        college = College.objects.get(id=college_id)
        serializer = CollegeSerializer(college)
        return Response(serializer.data)

class CourseDetail(APIView):

    def post(self, request):
        data = request.data
        if isinstance(data, list):
            serializer = CourseSerializer(data, many=True)
        else:
            serializer = CourseSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AllCourses(APIView):

    def post(self, request):
        courseObjs = Course.objects.select_related('college').filter(college_id=request.data['college_id'])
        return_obj = {}
        for courseObj in courseObjs:
                if not return_obj:
                    courses = []
                    courses.append({
                        'course_name': courseObj.course_name,
                        'avg_fees': courseObj.avg_fees
                    })
                    return_obj['college_name'] = courseObj.college.college_name
                    return_obj['avg_pkg'] = courseObj.college.avg_pkg
                    return_obj['rank'] = courseObj.college.rank
                    return_obj['Course'] = courses
                else:
                    return_obj['Course'].append({
                        'course_name':courseObj.course_name,
                        'avg_fees': courseObj.avg_fees
                    })
        if return_obj:
            return Response(return_obj, status=200)
        else:
            return Response(status=204)
