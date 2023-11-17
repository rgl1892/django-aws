from django.shortcuts import render, redirect
from .forms import DatasetForm
import boto3
from django.conf import settings


def index(request):
    client = boto3.client("s3")

    if request.method == "POST":
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            filename = (
                str(request.FILES["dataset"])
                .replace(" ", "_")
                .replace(")", "")
                .replace("(", "")
            )

            folder = request.POST["title"]
            bucket = settings.AWS_STORAGE_BUCKET_NAME
            old_name = f"1-RAW/Testing/django/{filename}"
            new_name = f"1-RAW/AD_HOC/ReadyForImport/{folder}/{filename}"

            client.copy_object(
                Bucket=bucket,
                CopySource={"Bucket": bucket, "Key": old_name},
                Key=new_name,
            )
            client.put_object_tagging(
                Bucket=bucket,
                Key=new_name,
                Tagging={
                    "TagSet": [
                        {
                            "Key": "personal_data",
                            "Value": request.POST["personal_data"],
                        },
                        {
                            "Key": "export_control",
                            "Value": request.POST["export_control"],
                        },
                        {
                            "Key": "national_security",
                            "Value": request.POST["national_security"],
                        },
                        {
                            "Key": "company_sensitve",
                            "Value": request.POST["company_sensitve"],
                        },
                        {
                            "Key": "business_private",
                            "Value": request.POST["business_private"],
                        },
                    ]
                },
            )
            client.delete_object(Bucket=bucket, Key=old_name)

            return redirect("home")
    else:
        form = DatasetForm()
    return render(
        request, "data_drop/index.html", {"form": form, "files": request.FILES}
    )
