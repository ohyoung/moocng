# -*- coding: utf-8 -*-
# Copyright 2013 Pablo Martín
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from celery import task

from moocng.courses.utils import clone_activiy_user_course


@task
def clone_activiy_user_course_task(user, course):
    clone_activiy_user_course(user, course)