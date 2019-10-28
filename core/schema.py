import graphene
from graphene_django import DjangoObjectType
from .models import Mahasiswa, Matakuliah

class MahasiswaType(DjangoObjectType):
    class Meta:
        model = Mahasiswa

class MatakuliahType(DjangoObjectType):
    class Meta:
        model = Matakuliah


class Query(graphene.ObjectType):
    all_mahasiswa = graphene.List(MahasiswaType)
    mahasiswa_by_id = graphene.Field(MahasiswaType, id=graphene.String(required=True))
    all_matakuliah = graphene.List(MatakuliahType)
    all_matakuliah_by_mahasiswaId = graphene.List(MatakuliahType, mahasiswa_id=graphene.String(required=True))

    def resolve_all_mahasiswa(parent, info):
        return Mahasiswa.objects.all()

    def resolve_mahasiswa_by_id(parent, info, **kwargs):
        return Mahasiswa.objects.get(id=kwargs.get('id'))

    def resolve_all_matakuliah(parent, info):
        return Matakuliah.objects.all()

    def resolve_all_matakuliah_by_mahasiswaId(parent, info, **kwargs):
        return Matakuliah.objects.filter(mahasiswaall_matakuliah_by_mahasiswaId=kwargs.get('mahasiswa_id'))



class CreateMahasiswa(graphene.Mutation):
    mahasiswa = graphene.Field(MahasiswaType)
    sukses = graphene.Boolean()
    class Input:
        nama = graphene.String(required=True)
        nim = graphene.String(required=True)

    def mutate(parent, info, **input):
        mahasiswa = Mahasiswa.objects.create(
            nama=input.get('nama'),
            nim=input.get('nim'),
        )
        mahasiswa.save()
        sukses=True

        return CreateMahasiswa(mahasiswa=mahasiswa, sukses=sukses)


class UpdateMahasiswa(graphene.Mutation):
    mahasiswa = graphene.Field(MahasiswaType)
    sukses = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)
        nama = graphene.String(required=True)
        nim = graphene.String(required=True)

    def mutate(parent, info, **input):
        mahasiswa = Mahasiswa.objects.get(id=input.get('id'))
        mahasiswa.nama=input.get('nama')
        mahasiswa.nim=input.get('nim')
        mahasiswa.save()
        sukses = True

        return UpdateMahasiswa(mahasiswa=mahasiswa, sukses=sukses)


class DeleteMahasiswa(graphene.Mutation):
    mahasiswa = graphene.Field(MahasiswaType)
    sukses = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)

    def mutate(parent, info, **input):
        mahasiswa = Mahasiswa.objects.get(
            id=input.get('id')
        )
        mahasiswa.delete()
        sukses = True

        return CreateMahasiswa(mahasiswa=mahasiswa, sukses=sukses)


class CreateMatakuliah(graphene.Mutation):
    matakuliah = graphene.Field(MatakuliahType)
    sukses = graphene.Boolean()

    class Input:
        nama = graphene.String(required=True)
        mahasiswa_id = graphene.String(required=True)

    def mutate(parent, info, **input):
        matakuliah = Matakuliah.objects.create(
            nama=input.get('nama'),
            mahasiswa_id=input.get('mahasiswa_id'),
        )
        matakuliah.save()
        sukses = True

        return CreateMatakuliah(matakuliah=matakuliah, sukses=sukses)


class UpdateMatakuliah(graphene.Mutation):
    matakuliah = graphene.Field(MatakuliahType)
    sukses = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)
        nama = graphene.String(required=True)
        mahasiswa_id = graphene.String(required=True)

    def mutate(parent, info, **input):
        matakuliah = Matakuliah.objects.get(id=input.get('id'))
        matakuliah.nama = input.get('nama')
        matakuliah.mahasiswa = input.get('mahasiswa_id')
        matakuliah.save()
        sukses = True

        return UpdateMahasiswa(matakuliah=matakuliah, sukses=sukses)


class DeleteMatakuliah(graphene.Mutation):
    mahasiswa = graphene.Field(MatakuliahType)
    sukses = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)

    def mutate(parent, info, **input):
        matakuliah = Matakuliah.objects.get(
            id=input.get('id')
        )
        matakuliah.delete()
        sukses = True

        return DeleteMatakuliah(matakuliah=matakuliah, sukses=sukses)


class Mutation(graphene.ObjectType):
    tambah_mahasiswa = CreateMahasiswa.Field()
    update_mahasiswa = UpdateMahasiswa.Field()
    delete_mahasiswa = DeleteMahasiswa.Field()
    tambah_matakuliah = CreateMatakuliah.Field()
    update_matakuliah = CreateMatakuliah.Field()
    delete_matakuliah = CreateMatakuliah.Field()

