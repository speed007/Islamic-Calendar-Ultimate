from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import hijri_converter
import pytz


cal = Calendar()

calendar_name = 'Islamic Calendar Ultimate'

cal.add('X-WR-CALNAME', calendar_name)  

month_mapping = {
    'Muharram': 1,
    'Safar': 2,
    'Rabi-ul-Awwal': 3,
    'Rabi al-Thani': 4,  
    'Jamadi-ul-Awwal': 5,
    'Jumada al-Thani': 6,
    'Rajab': 7,
    'Shaban': 8,
    'Ramadan': 9,
    'Shawwal': 10,
    'Zeelqadh': 11,
    'Dhu al-Hijja': 12
}

events = {
    '1 Muharram': 'Islamic New Year - Description: This day marks the beginning of the month of Muharram in the Islamic calendar.',
    '10 Muharram': 'Martyrdom of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ) - Description: Martyrdom of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ), the grandson of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), took place in the year 61 AH in Karbala, Iraq.',
    '20 Muharram': 'Demise of Sakina bint Imam Hussain (رَضِيَ ٱللهُ عَنْهُ) - Description: The demise of Sakina bint Imam Hussain (رَضِيَ ٱللهُ عَنْهُ), the beloved daughter of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ), occurred in the year 61 AH in the prison of Damascus, Syria.',
    '25 Muharram': 'Martyrdom of Imam Ali ibn Hussain Zain-ul-Abideen (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Ali ibn Hussain Zain-ul-Abideen (رَضِيَ ٱللهُ عَنْهُ), the son of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ) and the great-grandson of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was martyred in the year 95 AH in Medina, Saudi Arabia.',
    '1 Safar': 'First Day of Safar - Description: This day marks the beginning of the month of Safar in the Islamic calendar.',
    '24 Safar (or 16 Zilhaj)': 'Martyrdom of Zainab bint Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Zainab bint Ali (رَضِيَ ٱللهُ عَنْهُ), the daughter of Imam Ali (رَضِيَ ٱللهُ عَنْهُ) and the granddaughter of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), is believed to have been martyred in the year 62 AH.',
    '28 Safar': 'Martyrdom of Imam Hassan ibn Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Hassan ibn Ali (رَضِيَ ٱللهُ عَنْهُ), the grandson of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was martyred in the year 50 AH in Medina, Saudi Arabia.',
    '1 Rabi-ul-Awwal': 'First Day of Rabi-ul-Awwal - Description: This day marks the beginning of the month of Rabi-ul-Awwal in the Islamic calendar.',
    '12 Rabi-ul-Awwal': 'Birth of Holy Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) - Description: The birth of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), the final messenger of Islam, is celebrated on this day, believed to be in the year 570 AD in Mecca, Saudi Arabia.',
    '17 Rabi-ul-Awwal': 'Birth of Imam Jafar al-Sadiq (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Jafar al-Sadiq (رَضِيَ ٱللهُ عَنْهُ), Descendant of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was born in the year 83 AH in Medina, Saudi Arabia.',
    '1 Rabi al-Thani': 'First Day of Rabi al-Thani - Description: This day marks the beginning of the month of Rabi-ul-Awwal in the Islamic calendar.',
    '1 Jamadi-ul-Awwal': 'First Day of Jamadi-ul-Awwal - Description: This day marks the beginning of the month of Rabi-ul-Awwal in the Islamic calendar.',
    '15 Jamadi-ul-Awwal': 'Birth of Imam Ali ibn Hussain Zain-ul-Abideen (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Ali ibn Hussain Zain-ul-Abideen (رَضِيَ ٱللهُ عَنْهُ), Descendant of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was born on this day in the year 38 AH in Medina, Saudi Arabia.',
    '1 Jumada al-Thani': 'First Day of Jumada al-Thani- Description: This day marks the beginning of the month of Jumada al-Thani in the Islamic calendar.',
    '3 Jumada al-Thani': 'Demise of Fatima Zahra (رضي الله عنها) - Description: Fatima Zahra (رضي الله عنها), the daughter of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) and the wife of Imam Ali (رَضِيَ ٱللهُ عَنْهُ), passed away on this day in the year 11 AH in Medina, Saudi Arabia.',
    '20 Jumada al-Thani': 'Birth of Fatima Zahra (رضي الله عنها) - Description: Fatima Zahra (رضي الله عنها), the beloved daughter of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) and an esteemed figure in Islam, was born on this day in the year 615 AD in Mecca, Saudi Arabia.',
    '1 Rajab': 'First Day of Rajab - Description: This day marks the beginning of the month of Rajab in the Islamic calendar.',
    '13 Rajab': 'Birth of Commander of the Faithful, Ali ibn Abi Talib (رَضِيَ ٱللهُ عَنْهُ) - Description: "Maula Ali ibn Abi Talib (رَضِيَ ٱللهُ عَنْهُ), born on this day in the year 600 AD in Mecca, Saudi Arabia, is renowned as the Lion of Allah and the Gateway to the City of Knowledge.',
    '27 Rajab': 'Al Isra’ wal Mi’raj (The night journey and ascension) - Description: This event commemorates the night journey and ascension of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) to the heavens, which is believed to have taken place on this day.',
    '1 Shaban': 'First Day of Shaban - Description: This day marks the beginning of the month of Shaban in the Islamic calendar.',
    '1 Shaban': 'Birth of Zainab bint Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Zainab bint Ali (رَضِيَ ٱللهُ عَنْهُ), the daughter of Imam Ali (رَضِيَ ٱللهُ عَنْهُ) and the granddaughter of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was born on this day in the year 626 AD in Medina, Saudi Arabia.',
    '3 Shaban': 'Birth of Imam Hussain ibn Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Hussain ibn Ali (رَضِيَ ٱللهُ عَنْهُ), the third Imam of the Shia Muslims and the grandson of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was born on this day in the year 626 AD in Medina, Saudi Arabia.',
    '4 Shaban': 'Birth of Hazrat Abbas ibn Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Hazrat Abbas ibn Ali (رَضِيَ ٱللهُ عَنْهُ), the son of Imam Ali (رَضِيَ ٱللهُ عَنْهُ) and the brother of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ), was born on this day in the year 647 AD in Medina, Saudi Arabia.',
    '11 Shaban': 'Birth of Hazrat Ali Akbar ibn Hussain (رَضِيَ ٱللهُ عَنْهُ) - Description: Hazrat Ali Akbar ibn Hussain (رَضِيَ ٱللهُ عَنْهُ), the son of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ), was born on this day. He is remembered for his bravery and resemblance to his grandfather, Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ).',
    '15 Shaban': 'Shab-e-Barat - Description: Shab-e-Barat, also known as the Night of Forgiveness, is observed on the 15th night of the Islamic month of Shaban',
    '1 Ramadan': 'Ramadan begins - Description: This day marks the beginning of the month of Ramadan in the Islamic calendar',
    '8 Ramadan': 'Martyrdom of Hazrat Abu Talib (رَضِيَ ٱللهُ عَنْهُ) - Description: Hazrat Abu Talib (رَضِيَ ٱللهُ عَنْهُ), the uncle and protector of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), passed away on this day in the year 619 AD in Mecca, Saudi Arabia.',
    '10 Ramadan': 'Demise of Hazrat Khadija-tul-Kubra (رضي الله عنها) - Description: Hazrat Khadija-tul-Kubra (رضي الله عنها), the first wife of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) and the mother of the believers, passed away on this day in the year 619 AD in Mecca, Saudi Arabia.',
    '15 Ramadan': 'Birth of Imam Hassan ibn Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Hassan ibn Ali (رَضِيَ ٱللهُ عَنْهُ), the grandson of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was born on this day in the year 625 AD in Medina, Saudi Arabia.',
    '17 Ramadan': 'Demise of Sayyidah Aisha bint Abi Bakr (رَضِيَ ٱللهُ عَنْهُ) - Description: Sayyidah Aisha bint Abi Bakr (رَضِيَ ٱللهُ عَنْهُ), the wife of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) and a prominent figure in Islamic history, passed away on this day in the year 678 AD in Medina, Saudi Arabia.',
    '18 Ramadan': 'Night of the Attack on Commander of the Faithful, Ali (رَضِيَ ٱللهُ عَنْهُ), Maula Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: On this night, Lion of Allah Maula Ali ibn Abi Talib (رَضِيَ ٱللهُ عَنْهُ), was hurt by a poisoned sword while he was praying in the mosque in Kufa, Iraq.',
    '21 Ramadan': 'Martyrdom of Commander of the Faithful, Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Gateway to the City of Knowledge, Maula Ali ibn Abi Talib (رَضِيَ ٱللهُ عَنْهُ) was martyred on this day in the year 661 AD in Kufa, Iraq',
    '21 Ramadan': 'Night of Qadr (Revelation of Quran) - Description: Laylat al-Qadr, also known as the Night of Decree, is believed to be the night when the Quran was first revealed to Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ). It is considered the holiest night of the Islamic year.',
    '23 Ramadan': 'Night of Qadr (Revelation of Quran) - Description: Laylat al-Qadr, also known as the Night of Decree, is believed to be the night when the Quran was first revealed to Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ). It is considered the holiest night of the Islamic year.',
    '25 Ramadan': 'Night of Qadr (Revelation of Quran) - Description: Laylat al-Qadr, also known as the Night of Decree, is believed to be the night when the Quran was first revealed to Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ). It is considered the holiest night of the Islamic year.',
    '27 Ramadan': 'Night of Qadr (Revelation of Quran) - Description: Laylat al-Qadr, also known as the Night of Decree, is believed to be the night when the Quran was first revealed to Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ). It is considered the holiest night of the Islamic year.',
    '29 Ramadan': 'Night of Qadr (Revelation of Quran) - Description: Laylat al-Qadr, also known as the Night of Decree, is believed to be the night when the Quran was first revealed to Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ). It is considered the holiest night of the Islamic year.',
    '1 Shawwal': 'Eid al-Fitr - Description: Eid al-Fitr is the festival celebrated by Muslims worldwide to mark the end of the month of Ramadan and the beginning of Shawwal.',
    '15 Shawwal': 'Martyrdom of Imam Jafar al-Sadiq (رَضِيَ ٱللهُ عَنْهُ) - Description: Imam Jafar al-Sadiq (رَضِيَ ٱللهُ عَنْهُ), the descendant of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), was martyred on this day in the year 148 AH in Medina, Saudi Arabia.',
    '1 Zeelqadh': 'First Day of Zeelqadh - Description: This day marks the beginning of the month of Zeelqadh in the Islamic calendar.',
    '1 Dhu al-Hijja': 'Dhu al-Hijja begins - Description: This day marks the beginning of the month of Dhu al-Hijja in the Islamic calendar.',
    '1 Dhu al-Hijja': 'Marriage of Fatima Zahra (رضي الله عنها) & Commander of the Faithful, Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: The marriage of Fatima Zahra (رضي الله عنها), the daughter of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), and Imam Ali ibn Abi Talib (رَضِيَ ٱللهُ عَنْهُ), the first Imam of the Shia Muslims, took place on this day.',
    '8 Dhu al-Hijja': 'Hajj begins - Description: The annual pilgrimage of Hajj, one of the five pillars of Islam, begins on this day in Mecca, Saudi Arabia.',
    '9 Dhu al-Hijja': 'Day of ‘Arafah - Description: The Day of ‘Arafah is considered one of the most important and sacred days in the Islamic calendar, observed during the Hajj pilgrimage.',
    '9 Dhu al-Hijja': 'Martyrdom of Muslim ibn Aqil (رَضِيَ ٱللهُ عَنْهُ) - Description: Muslim ibn Aqil (رَضِيَ ٱللهُ عَنْهُ), the cousin and emissary of Imam Hussain (رَضِيَ ٱللهُ عَنْهُ), was martyred on this day in the year 60 AH in Kufa, Iraq.',
    '10 Dhu al-Hijja': 'Eid al-Adha - Description: Eid al-Adha, also known as the Festival of Sacrifice, is celebrated by Muslims worldwide on this day, commemorating the willingness of Prophet Ibrahim (رَضِيَ ٱللهُ عَنْهُ) to sacrifice his son as an act of obedience to God.',
    '16 Dhu al-Hijja (or 24 Safar)': 'Martyrdom of Zainab bint Ali (رَضِيَ ٱللهُ عَنْهُ) - Description: Zainab bint Ali (رَضِيَ ٱللهُ عَنْهُ), the daughter of Imam Ali (رَضِيَ ٱللهُ عَنْهُ) and the granddaughter of Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ), is believed to have been martyred on this day.',
    '22 Dhu al-Hijja': 'Martyrdom of the Children of Hazrat Muslim ibn Aqil (رَضِيَ ٱللهُ عَنْهُ) - Description: The children of Hazrat Muslim ibn Aqil (رَضِيَ ٱللهُ عَنْهُ), who were martyred in the aftermath of their father’s death, are remembered on this day.',
    '24 Dhu al-Hijja': 'Event of the mubahala - Description: the event of Mubahela, a public debate and invocation for divine curse to reveal the truth, which took place between Prophet Muhammad (صَلَّى ٱللَّٰهُ عَلَيْهِ وَسَلَّمَ) and a Christian delegation from Najran.'
}  

for islamic_date, full_event_description in events.items():
    parts = islamic_date.split()
    days = parts[0].split(',')
    if parts[1] in ['Rabi', 'Jumada', 'Dhu']:
        month_name = ' '.join(parts[1:3])
    else:
        month_name = parts[1]

    month = month_mapping[month_name]

    for day in days:
        gregorian_date = hijri_converter.convert.Hijri(1445, month, int(day)).to_gregorian()

        event = Event()

        if ' - Description: ' in full_event_description:
            event_name, event_description = full_event_description.split(' - Description: ')
        else:
            event_name = full_event_description
            event_description = ''  

        if '–' in event_description:
            event_description = event_description.split('–')[0].strip()

        event.add('summary', f"{islamic_date} - {event_name}")
        event.add('description', event_description.strip())

        start_time = datetime(gregorian_date.year, gregorian_date.month, gregorian_date.day)
        event.add('dtstart', start_time.date())  
        event.add('dtend', (start_time + timedelta(days=1)).date())  
        
        alarm_24hr = Alarm()
        alarm_24hr.add('action', 'DISPLAY')
        alarm_24hr.add('description', f'Reminder: {event_name}')
        alarm_24hr.add('trigger', timedelta(hours=-24))
        event.add_component(alarm_24hr)

        alarm_12hr = Alarm()
        alarm_12hr.add('action', 'DISPLAY')
        alarm_12hr.add('description', f'Reminder: {event_name}')
        alarm_12hr.add('trigger', timedelta(hours=-12))
        event.add_component(alarm_12hr)

    cal.add_component(event)
