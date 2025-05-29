from django.shortcuts import render, redirect
from django.core.mail import send_mail
from ping3 import ping
from datetime import datetime

# This acts like in-memory database (will reset on server restart)
devices = {
    '192.224.1.1': {'name': 'Router', 'status': 'Unknown', 'last_checked': ''},
    '192.348.1.2': {'name': 'Switch', 'status': 'Unknown', 'last_checked': ''},
    '8.8.8.8': {'name': 'Google DNS', 'status': 'Unknown', 'last_checked': ''},
    '1.1.1.1': {'name': 'Cloudflare DNS', 'status': 'Unknown', 'last_checked': ''},
}

def send_offline_alert(device_name, ip):
    send_mail(
        subject=f'Alert: {device_name} ({ip}) is Offline!',
        message=f'The device {device_name} with IP {ip} is currently offline as of {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.',
        from_email='rroy1836@gmail.com',
        recipient_list=['alert-recipient@example.com'],
        fail_silently=False,
    )

def dashboard(request):
    # Handle new device submission
    if request.method == 'POST':
        ip = request.POST.get('ip')
        name = request.POST.get('name')
        if ip and name and ip not in devices:
            devices[ip] = {'name': name, 'status': 'Unknown', 'last_checked': ''}

        # Redirect after POST to prevent form resubmission
        return redirect('dashboard')

    # Ping all devices and update status
    for ip, info in devices.items():
        try:
            response = ping(ip, timeout=1, unit='ms')
            status = 'Online' if response else 'Offline'
        except Exception as e:
            status = 'Offline'
            print(f"Error pinging {ip}: {e}")
        info['status'] = status
        info['last_checked'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    return render(request, 'monitor/dashboard.html', {'devices': devices})

def delete_device(request, ip):
    if ip in devices:
        del devices[ip]
    return redirect('dashboard')

def edit_device(request, ip):
    if request.method == "POST":
        new_name = request.POST.get("name")
        if ip in devices:
            devices[ip]['name'] = new_name
        return redirect('dashboard')
    return render(request, "edit_device.html", {"ip": ip, "device": devices.get(ip)})