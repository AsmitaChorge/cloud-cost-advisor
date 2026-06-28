from flask import Flask, render_template, request
import json

from services.pricing_service import PricingService

app = Flask(__name__)

pricing_service = PricingService()

def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


@app.route("/")
def home():
    return render_template(
        "index.html",
        regions=load_json("data/regions.json"),
        instances=load_json("data/ec2_instances.json"),
        operating_systems=load_json("data/operating_systems.json")
    )


@app.route("/calculate", methods=["POST"])
def calculate():

    region = request.form["region"]
    instance = request.form["instance"]
    operating_system = request.form["operating_system"]
    hours = int(request.form["hours"])

    hourly_price = pricing_service.get_price(
        "EC2",
        region,
        instance,
        operating_system
    )

    monthly_cost = round(hourly_price * hours, 2)

    return render_template(
    "result.html",
    region=region,
    instance=instance,
    operating_system=operating_system,
    hours=hours,
    hourly_price=hourly_price,
    monthly_cost=monthly_cost
)


if __name__ == "__main__":
    app.run(debug=True)