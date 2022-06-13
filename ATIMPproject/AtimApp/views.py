from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db import connection
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import UniversitySerializer, CompanySerializer, Graduete_StudentsSerializer, Job_OfferSerializer
from .models import University, Company, Graduete_Students, Job_Offer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_university(request: Request):
    """A simple function that add university to the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.add_university'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    new_university = UniversitySerializer(data=request.data)
    if new_university.is_valid():
        new_university.save()
        return Response({"University": new_university.data})
    else:
        print(new_university.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def display_university(request: Request):
    """A simple function that display all universities in the system"""
    university = University.objects.all()
    data = {
        'msg': 'Display All Universities',
        'University': UniversitySerializer(instance=university, many=True).data
    }
    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_university(request: Request, university_id):
    """A simple function that update university in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.change_university'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    university = University.objects.get(id=university_id)
    request.data.update(user=request.user.id)
    updated_university = UniversitySerializer(instance=university, data=request.data)
    if updated_university.is_valid():
        updated_university.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_university.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_university(request: Request, university_id):
    """A simple function that delete university from the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.delete_university'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    university = University.objects.get(id=university_id)
    university.delete()
    return Response({"msg": "Delete it successfully"})


# ----------------------------------------------------------------------
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_company(request: Request):
    """A simple function that add company to the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.add_company'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    new_company = CompanySerializer(data=request.data)
    if new_company.is_valid():
        new_company.save()
        return Response({"Company": new_company.data})
    else:
        print(new_company.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def display_company(request: Request):
    """A simple function that display all companies in the system"""
    company = Company.objects.all()
    data = {
        'msg': 'Display All Companies',
        'Company': CompanySerializer(instance=company, many=True).data
    }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def graduate_student_info_by_university(request: Request):
    """A simple function that display graduate student information depend on his university from the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.view_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if University.objects.filter(user=request.user.id).exists():
        university_name = University.objects.get(user=request.user.id)
        if Graduete_Students.objects.filter(university=university_name.id).exists():
            student_info1 = Graduete_Students.objects.filter(university=university_name.id)
            data = {
                'university': Graduete_StudentsSerializer(instance=student_info1, many=True).data,
            }
        else:
            data = {
                'msg': 'not found any student '
            }
    else:
        data = {
            'msg': 'not found it ',
        }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def graduate_status_by_university(request: Request, student_id):
    """A simple function that display graduate student status depend on his university from the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.view_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if University.objects.filter(user=request.user.id).exists():
        if Job_Offer.objects.filter(student_id=student_id).exists():
            job_offer = Job_Offer.objects.filter(student_id=student_id)
            data = {
                'university': Job_OfferSerializer(instance=job_offer, many=True).data,
            }
        else:
            data = {
                'msg': 'not found any job offer '
            }
    else:
        data = {
            'msg': 'not found any student',
        }
    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_company(request: Request, company_id):
    """A simple function that update company in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.change_company'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    company = Company.objects.get(id=company_id)
    request.data.update(user=request.user.id)
    updated_company = CompanySerializer(instance=company, data=request.data)
    if updated_company.is_valid():
        updated_company.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_company.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_company(request: Request, company_id):
    """A simple function that delete company in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.delete_company'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    company = Company.objects.get(id=company_id)
    company.delete()
    return Response({"msg": "Delete it successfully"})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def display_all_graduate_student(request: Request):
    """A simple function that display all graduate student in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.view_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    graduate = Graduete_Students.objects.all()
    data = {
        'msg': 'Display All Graduate Students',
        'Graduate': Graduete_StudentsSerializer(instance=graduate, many=True).data
    }
    return Response(data)


# -----------------------------------------------------------------
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_graduate_student(request: Request):
    """A simple function that add graduate student in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.add_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data.update(user=request.user.id)
    new_graduate_student = Graduete_StudentsSerializer(data=request.data)
    if new_graduate_student.is_valid():
        new_graduate_student.save()
        return Response({"Graduate": new_graduate_student.data})
    else:
        print(new_graduate_student.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def display_graduate_student(request: Request):
    """A simple function that display graduate student by register them in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.view_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    graduate = Graduete_Students.objects.filter(user=request.user.id)
    data = {
        'msg': 'Display All Graduate Students',
        'Graduate': Graduete_StudentsSerializer(instance=graduate, many=True).data
    }
    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_graduate_student(request: Request, student_id):
    """A simple function that update graduate student in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.change_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    graduate = Graduete_Students.objects.get(id=student_id)
    request.data.update(user=request.user.id)
    updated_graduate = Graduete_StudentsSerializer(instance=graduate, data=request.data)
    if updated_graduate.is_valid():
        updated_graduate.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_graduate.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_graduate_student(request: Request, student_id):
    """A simple function that delete graduate student in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.delete_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    graduate = Graduete_Students.objects.get(id=student_id)
    graduate.delete()
    return Response({"msg": "Delete it successfully"})


# ------------------------------------------------------------------------------
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_job_offer(request: Request):
    """A simple function that add job offer to the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.add_job_offer'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    # request.data.update(user=request.user.id)
    new_offer = Job_OfferSerializer(data=request.data)
    if new_offer.is_valid():
        new_offer.save()
        return Response({"Job Offer": new_offer.data})
    else:
        print(new_offer.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def Search_by_major(request: Request, major):
    """A simple function that search about student by major  in the system"""
    students = Graduete_Students.objects.filter(major=major)
    if students.exists():
        return Response({"msg": Graduete_StudentsSerializer(instance=students, many=True).data})
    else:
        return Response({"msg": "Not found !!"})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def display_graduate_student_status(request: Request):
    """A simple function that all graduated student with status in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.view_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    graduate = Graduete_Students.objects.all()
    job_offer = Job_Offer.objects.all()
    data = {
        'msg': 'Display All Graduate Students',
        'Graduate': Graduete_StudentsSerializer(instance=graduate, many=True).data,
        'Job offer': Job_OfferSerializer(instance=job_offer, many=True).data
    }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_profile(request: Request):
    """A simple function that display the information and status about specific student in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.view_graduete_students'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if Graduete_Students.objects.filter(email=request.user.email).exists():
        student_info1 = Graduete_Students.objects.filter(email=request.user.email)
        student_info = Graduete_Students.objects.get(email=request.user.email)
        print(Job_Offer.objects.filter(student_id=request.user.id).exists())
        print(request.user.id)
        if Job_Offer.objects.filter(student_id=student_info.id).exists():
            job_offer = Job_Offer.objects.filter(student_id=student_info.id)
            data = {
                'msg': 'Display All Graduate Students',
                'Graduate': Graduete_StudentsSerializer(instance=student_info1, many=True).data,
                'job_offer': Job_OfferSerializer(instance=job_offer, many=True).data
            }
        else:
            data = {
                'msg': 'Display All Graduate Students',
                'Graduate': Graduete_StudentsSerializer(instance=student_info1, many=True).data,
                'job_offer': "This job offer is not intended for you"
            }
    else:
        data = {
            'msg': 'not found it ',
        }
    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_student_profile(request: Request, offer_id):
    """A simple function that update splay the information and status about specific student in the system"""
    if not request.user.is_authenticated or not request.user.has_perm('AtimApp.change_job_offer'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    if Graduete_Students.objects.filter(email=request.user.email).exists():
        student = Graduete_Students.objects.get(email=request.user.email)
        request.data["student"] = student.id
        offer = Job_Offer.objects.get(id=offer_id)
        updated_job_offer = Job_OfferSerializer(instance=offer, data=request.data)
        if updated_job_offer.is_valid():
            updated_job_offer.save()

            data = {
                "msg": "updated successfully"
            }

            return Response(data)
        else:
            print(updated_job_offer.errors)
            return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

    else:
        data = {
            'msg': 'not found it ',
        }
    return Response(data)
