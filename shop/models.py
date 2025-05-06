# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clinic(models.Model):
    clinic_id = models.AutoField(db_column='ClinicID', primary_key=True)  # Field name made lowercase.
    clinic_name = models.CharField(db_column='ClinicName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Clinic'


class ClinicAdmin(models.Model):
    admin_id = models.AutoField(db_column='AdminID', primary_key=True)  # Field name made lowercase.
    clinic_id = models.ForeignKey(Clinic, models.DO_NOTHING, db_column='ClinicID', blank=True, null=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='AdminName', max_length=255)  # Field name made lowercase.
    admin_info = models.TextField(db_column='AdminInfo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ClinicAdmin'


class DeviceMeasurements(models.Model):
    measurement_id = models.AutoField(db_column='MeasurementID', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    examination_id = models.ForeignKey('Medicalexamination', models.DO_NOTHING, db_column='ExaminationID', blank=True, null=True)  # Field name made lowercase.
    device_type = models.CharField(db_column='DeviceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DeviceMeasurements'


class Doctor(models.Model):
    doctor_id = models.AutoField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctor_info = models.TextField(db_column='DoctorInfo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    clinic_id = models.ForeignKey(Clinic, models.DO_NOTHING, db_column='ClinicID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'Doctor'


class Image(models.Model):
    image_id = models.AutoField(db_column='ImageID', primary_key=True)  # Field name made lowercase.
    examination_id = models.ForeignKey('Medicalexamination', models.DO_NOTHING, db_column='ExaminationID', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    image_data = models.TextField(db_column='ImageData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Image'


class Job(models.Model):
    job_id = models.AutoField(db_column='JobID', primary_key=True)  # Field name made lowercase.
    job_name = models.CharField(db_column='JobName', unique=True, max_length=100)  # Field name made lowercase.
    job_type = models.CharField(db_column='JobType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workhours = models.IntegerField(db_column='WorkHours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Job'


class Location(models.Model):
    location_id = models.AutoField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='LocationName', max_length=100)  # Field name made lowercase.
    location_city = models.CharField(db_column='LocationCity', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Location'


class MedicalExamination(models.Model):
    examination_id = models.AutoField(db_column='ExaminationID', primary_key=True)  # Field name made lowercase.
    patient_id = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    doctor_id = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    terminal_id = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='TerminalID', blank=True, null=True)  # Field name made lowercase.
    result = models.TextField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MedicalExamination'


class Patient(models.Model):
    patient_id = models.AutoField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    medical_info = models.TextField(db_column='MedicalInfo', blank=True, null=True)  # Field name made lowercase.
    jobid = models.ForeignKey(Job, models.DO_NOTHING, db_column='JobID', blank=True, null=True)  # Field name made lowercase.
    client_organization_id = models.ForeignKey(Clinic, models.DO_NOTHING, db_column='ClientOrganizationID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'Patient'


class Terminal(models.Model):
    terminal_id = models.AutoField(db_column='TerminalID', primary_key=True)  # Field name made lowercase.
    location_id = models.ForeignKey(Location, models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service_info = models.TextField(db_column='ServiceInfo', blank=True, null=True)  # Field name made lowercase.
    clinic_id = models.ForeignKey(Clinic, models.DO_NOTHING, db_column='ClinicID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'Терминал №{self.terminal_id}'

    class Meta:
        managed = True
        db_table = 'Terminal'
