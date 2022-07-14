import typing
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    scope: typing.Mapping[str, str]

    receive: typing.Callable[[], typing.Awaitable[object]]
    send: typing.Callable[[object], typing.Awaitable[None]]


class Staff:
    def __init__(self):
        self.staff = {}

    def register_worker(self, request):
        self.staff[request.scope["id"]] = Worker(request)

    def deregister_worker(self, id_):
        self.staff.pop(id_)

    def export(self):
        return {key: value.request for key, value in self.staff.items()}

    def workers_by_speciality(self):
        dct = defaultdict(list)
        for id_, worker in self.staff.items():
            dct[worker.speciality].append(worker.id_)
        return dct

    async def process_request(self, request: Request):
        workers_by_speciality_ = self.workers_by_speciality()
        speciality = request.scope["speciality"]
        worker_id = workers_by_speciality_[speciality][0]
        self.register_worker(self.staff.pop(worker_id).request)
        await self.staff[worker_id].process_request(request)


class Worker:
    def __init__(self, request: Request):
        self.id_ = request.scope["id"]
        self.speciality = request.scope["speciality"]
        self.receive = request.receive
        self.send = request.send
        self.request = request

    async def process_request(self, request: Request):
        full_order = await request.receive()
        await self.send(full_order)

        result = await self.receive()
        await request.send(result)


class RestaurantManager:
    def __init__(self):
        """Instantiate the restaurant manager.

        This is called at the start of each day before any staff get on
        duty or any orders come in. You should do any setup necessary
        to get the system working before the day starts here; we have
        already defined a staff dictionary.
        """
        self.staff_ = Staff()

    @property
    def staff(self):
        return self.staff_.export()

    async def __call__(self, request: Request):
        """Handle a request received.

        This is called for each request received by your application.
        In here is where most of the code for your system should go.

        :param request: request object
            Request object containing information about the sent
            request to your application.
        """
        type_ = request.scope["type"]

        if 'staff.' in type_:
            id_ = request.scope["id"]
            match type_:
                case "staff.onduty":
                    self.staff_.register_worker(request)
                case "staff.offduty":
                    self.staff_.deregister_worker(id_)

        elif type_ == "order":
            await self.staff_.process_request(request)
