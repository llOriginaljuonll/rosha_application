from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from core.mixins import IsStaffMixin
from apps.events.participation.models import Participation
from apps.performer.participant.forms import ParticipantForm
 
class ParticipantFormView(IsStaffMixin, UpdateView):
    """
    class นี้ ได้ใช้ UpdateView แทนการใช้ UpdateView
    - จำเหตุผลไม่ได้ว่าทำไม
    - แต่คิดตามความเป็น make sense แล้ว มันควรเป็น CreateView มากกว่า
    - ในอนาคตจะทำการเปลี่ยน <!-- วันที่ทำความเห็น 5 Nov, 2024

    * ควรเปลี่ยนตำแหน่งการ reverse_lazy ไปตำแหน่งอื่น เพราะเบื้องต้นตอนนี้ เราไม่ได้ต้องการให้ผู้ที่ทำการผ่านการเข้ารอบ เข้าถึงหน้า participant list page <!-- สามารถไปพัฒนาต่อได้ -->

    properties:
        context['form'] = self.get_form() เป็นการเพิ่มฟอร์มใน context ปกติใน context มี key form อยู๋แล้ว เหมือนกับการ overriding อีกครั้ง
    """
    model = Participation
    form_class = ParticipantForm
    template_name = 'performer/participants/participant_form.html'
    context_object_name = 'participation'

    def get_success_url(self):
        return reverse_lazy('participation:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context