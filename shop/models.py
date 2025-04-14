# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clinic(models.Model):
    clinicid = models.IntegerField(db_column='ClinicID', primary_key=True)  # Field name made lowercase.
    clinicname = models.CharField(db_column='ClinicName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clinic'


class Clinicadmin(models.Model):
    adminid = models.IntegerField(db_column='AdminID', primary_key=True)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinic, models.DO_NOTHING, db_column='ClinicID', blank=True, null=True)  # Field name made lowercase.
    adminname = models.CharField(db_column='AdminName', max_length=255)  # Field name made lowercase.
    admininfo = models.TextField(db_column='AdminInfo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicAdmin'


class Devicemeasurements(models.Model):
    measurementid = models.IntegerField(db_column='MeasurementID', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    examinationid = models.ForeignKey('Medicalexamination', models.DO_NOTHING, db_column='ExaminationID', blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeviceMeasurements'


class Doctor(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctorinfo = models.TextField(db_column='DoctorInfo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    clinicid = models.ForeignKey(Clinic, models.DO_NOTHING, db_column='ClinicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctor'


class Image(models.Model):
    imageid = models.IntegerField(db_column='ImageID', primary_key=True)  # Field name made lowercase.
    examinationid = models.ForeignKey('Medicalexamination', models.DO_NOTHING, db_column='ExaminationID', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    imagedata = models.TextField(db_column='ImageData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Image'


class Job(models.Model):
    jobid = models.IntegerField(db_column='JobID', primary_key=True)  # Field name made lowercase.
    jobname = models.CharField(db_column='JobName', unique=True, max_length=100)  # Field name made lowercase.
    jobtype = models.CharField(db_column='JobType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workhours = models.IntegerField(db_column='WorkHours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Job'


class Location(models.Model):
    locationid = models.IntegerField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', max_length=100)  # Field name made lowercase.
    locationcity = models.CharField(db_column='LocationCity', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Medicalexamination(models.Model):
    examinationid = models.IntegerField(db_column='ExaminationID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    terminalid = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='TerminalID', blank=True, null=True)  # Field name made lowercase.
    result = models.TextField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MedicalExamination'


class Patient(models.Model):
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    medicalinfo = models.TextField(db_column='MedicalInfo', blank=True, null=True)  # Field name made lowercase.
    jobid = models.ForeignKey(Job, models.DO_NOTHING, db_column='JobID', blank=True, null=True)  # Field name made lowercase.
    clientorganizationid = models.IntegerField(db_column='ClientOrganizationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'


class Terminal(models.Model):
    terminalid = models.IntegerField(db_column='TerminalID', primary_key=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serviceinfo = models.TextField(db_column='ServiceInfo', blank=True, null=True)  # Field name made lowercase.
    clinicid = models.IntegerField(db_column='ClinicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Terminal'
