import platform
import os
import subprocess

def intrusive_reminder(title, message):
    # Platform-specific notifications
    if platform.system() == 'Darwin':  # macOS
        # Use AppleScript for macOS notifications
        apple_script = f'''
        display notification "{message}" with title "{title}"
        '''
        subprocess.run(['osascript', '-e', apple_script])
        
        # Add a popup dialog that requires interaction
        dialog_script = f'''
        tell application "System Events"
            display dialog "{message}" with title "{title}" buttons {{"OK"}} default button "OK" with icon caution giving up after 86400
        end tell
        '''
        subprocess.run(['osascript', '-e', dialog_script])
        
    elif platform.system() == 'Windows':
        # Use Windows notification (this is a fallback if you ever run on Windows)
        os.system(f'powershell -command "[reflection.assembly]::loadwithpartialname(\'System.Windows.Forms\');[System.Windows.Forms.MessageBox]::Show(\'{message}\',\'{title}\')"')
    else:  # Linux and other platforms
        # Simple terminal notification for Linux
        os.system(f'notify-send "{title}" "{message}"')

# Simply run the reminder when the script is executed
intrusive_reminder("College Payment", "Don't forget to pay your college fees today!")